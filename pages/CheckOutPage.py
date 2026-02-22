import re

from faker import Faker

from pages.BasePage import BasePage
from pages.RegisterPage import Address


class CheckOutPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.faker: Faker = context.faker

        # --- Selectores ---
        self.PROCEED_TO_CHECKOUT_BUTTON = "div a.btn.btn-default.check_out"
        self.CARD_NAME_INPUT = "input[data-qa='name-on-card']"
        self.CARD_NUMBER_INPUT = "input[data-qa='card-number']"
        self.CVC_INPUT = "input[data-qa='cvc']"
        self.EXPIRY_MONTH_INPUT = "input[data-qa='expiry-month']"
        self.EXPIRY_YEAR_INPUT = "input[data-qa='expiry-year']"
        self.PAY_BUTTON = "button[data-qa='pay-button']"
        self.DOWNLOAD_INVOICE_LINK = "a[href^='/download_invoice/']"

    def click_proceed_to_checkout_button(self):
        self.click_element(self.PROCEED_TO_CHECKOUT_BUTTON)

    def click_place_order_button(self):
        self.click_element(self.PROCEED_TO_CHECKOUT_BUTTON)

    def fill_payment_formulary(self, nombre_tarjeta, numero_tarjeta, cvc, mes_expiracion, anio_expiracion):
        self.fill_input(self.CARD_NAME_INPUT, nombre_tarjeta)
        self.fill_input(self.CARD_NUMBER_INPUT, numero_tarjeta)
        self.fill_input(self.CVC_INPUT, cvc)
        self.fill_input(self.EXPIRY_MONTH_INPUT, mes_expiracion)
        self.fill_input(self.EXPIRY_YEAR_INPUT, anio_expiracion)

    def click_pay_and_confirm_order(self):
        self.click_element(self.PAY_BUTTON)

    def verify_address(self, address_data: Address):
        self.verify_text_in_page(address_data.address_data)
        self.verify_text_in_page(address_data.address2_data)
        self.verify_text_in_page(address_data.zipcode_data)
        self.verify_text_in_page(address_data.city_data)
        self.verify_text_in_page(address_data.state_data)
        self.verify_text_in_page(address_data.country_data)

    def download_invoice(self):
        with self.page.expect_download() as download_info:
            self.click_element(self.DOWNLOAD_INVOICE_LINK)

        download = download_info.value
        path = download.path()

        with open(path, "rb") as f:
            content = f.read()
            assert len(content) > 0, "El archivo está vacío"

            pattern = re.compile(rb"Your total purchase amount is \d+\.?(\d+)?\.? Thank you")
            assert pattern.search(content)
