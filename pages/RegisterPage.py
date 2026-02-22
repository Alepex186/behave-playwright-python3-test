from faker import Faker

from pages.BasePage import BasePage


class Address:
    def __init__(self, address_data, address2_data, zipcode_data, city_data, state_data):
        self.address_data = address_data
        self.address2_data = address2_data
        self.zipcode_data = zipcode_data
        self.city_data = city_data
        self.state_data = state_data
        self.country_data = None

    def set_country_data(self, country):
        self.country_data = country


class RegisterPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.faker: Faker = self.context.faker

        # --- Selectores: Formulario inicial ---
        self.NAME_INPUT = "[data-qa='signup-name']"
        self.EMAIL_INPUT = "[data-qa='signup-email']"
        self.SIGNUP_BUTTON = "[data-qa='signup-button']"

        # --- Selectores: Formulario principal ---
        self.TITLE_GENDER_RADIO = "//input[@type='radio' and @id='id_gender1']"
        self.PASSWORD_INPUT = "[data-qa='password']"
        self.DOB_DAYS_SELECT = "[data-qa='days']"
        self.DOB_MONTHS_SELECT = "[data-qa='months']"
        self.DOB_YEARS_SELECT = "[data-qa='years']"
        self.FIRST_NAME_INPUT = "[data-qa='first_name']"
        self.LAST_NAME_INPUT = "[data-qa='last_name']"
        self.ADDRESS_INPUT = "[data-qa='address']"
        self.ADDRESS2_INPUT = "[data-qa='address2']"
        self.COUNTRY_SELECT = "[data-qa='country']"
        self.STATE_INPUT = "[data-qa='state']"
        self.CITY_INPUT = "[data-qa='city']"
        self.ZIPCODE_INPUT = "[data-qa='zipcode']"
        self.MOBILE_NUMBER_INPUT = "[data-qa='mobile_number']"
        self.CREATE_ACCOUNT_BUTTON = "[data-qa='create-account']"

        # --- Datos de dirección generados ---
        self.address_data = Address(
            self.faker.address(),
            self.faker.secondary_address(),
            self.faker.zipcode(),
            self.faker.city(),
            self.faker.state()
        )

    def fill_firtsname(self, nombre=None):
        name = nombre if nombre else self.faker.first_name()
        self.fill_input(self.NAME_INPUT, name)

    def fill_email(self, correo=None):
        email = correo if correo else self.faker.email()
        self.fill_input(self.EMAIL_INPUT, email)

    def click_signup_button(self):
        self.click_element(self.SIGNUP_BUTTON)

    def fill_formulary(self):
        self.click_element(self.TITLE_GENDER_RADIO)
        self.fill_input(self.PASSWORD_INPUT, "123456789")
        self.select_option(self.DOB_DAYS_SELECT, index=2)
        self.select_option(self.DOB_MONTHS_SELECT, index=2)
        self.select_option(self.DOB_YEARS_SELECT, index=2)
        self.fill_input(self.FIRST_NAME_INPUT, self.faker.first_name())
        self.fill_input(self.LAST_NAME_INPUT, self.faker.last_name())
        self.fill_input(self.ADDRESS_INPUT, self.address_data.address_data)
        self.fill_input(self.ADDRESS2_INPUT, self.address_data.address2_data)

        self.select_option(self.COUNTRY_SELECT, index=1)
        self.address_data.set_country_data(self.get_input_value(self.COUNTRY_SELECT))

        self.fill_input(self.STATE_INPUT, self.address_data.state_data)
        self.fill_input(self.CITY_INPUT, self.address_data.city_data)
        self.fill_input(self.ZIPCODE_INPUT, self.address_data.zipcode_data)
        self.fill_input(self.MOBILE_NUMBER_INPUT, "+12125550123")

    def click_create_account_button(self):
        self.click_element(self.CREATE_ACCOUNT_BUTTON)
