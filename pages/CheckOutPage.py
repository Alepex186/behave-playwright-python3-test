import re

from faker import Faker
from playwright.sync_api import Page

from pages.RegisterPage import Address


class CheckOutPage:
    def __init__(self,context):
        self.page:Page=context.page
        self.faker:Faker=context.faker

    def click_proceed_to_checkout_button(self):
        button=self.page.locator("div a.btn.btn-default.check_out")
        button.click()

    def verify_text_in_page(self, text):
        locator = self.page.locator(f"text={text}")
        assert locator.count() > 0, f"No se encontró el texto: {text}"

    def click_place_order_button(self):
        button=self.page.locator("div a.btn.btn-default.check_out")
        button.click()

    def fill_payment_formulary(self, nombre_tarjeta, numero_tarjeta, cvc, mes_expiracion, anio_expiracion):
        card_name_input=self.page.locator("input[data-qa='name-on-card']")
        card_number_input=self.page.locator("input[data-qa='card-number']")
        cvc_input=self.page.locator("input[data-qa='cvc']")
        expiry_month=self.page.locator("input[data-qa='expiry-month']")
        expiry_year=self.page.locator("input[data-qa='expiry-year']")

        card_name_input.fill(nombre_tarjeta)
        card_number_input.fill(numero_tarjeta)
        cvc_input.fill(cvc)
        expiry_month.fill(mes_expiracion)
        expiry_year.fill(anio_expiracion)

    def click_pay_and_confirm_order(self):
        pay_and_confirm_order_button=self.page.locator("button[data-qa='pay-button']")
        pay_and_confirm_order_button.click()

    def verify_address(self, address_data:Address):
        self.verify_text_in_page(address_data.address_data)
        self.verify_text_in_page(address_data.address2_data)
        self.verify_text_in_page(address_data.zipcode_data)
        self.verify_text_in_page(address_data.city_data)
        self.verify_text_in_page(address_data.state_data)
        self.verify_text_in_page(address_data.country_data)


    def download_invoice(self):
        with self.page.expect_download() as download_info:
            self.page.click("a[href^='/download_invoice/']")

        download = download_info.value
        path = download.path()
        filename = download.suggested_filename

        with open(path, "rb") as f:
            content = f.read()
            assert len(content) > 0, "El archivo está vacío"

            pattern = re.compile(rb"Your total purchase amount is \d+\.?(\d+)?\.? Thank you")

            assert pattern.search(content)
