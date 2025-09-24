from faker import Faker


class RegisterPage:
    def __init__(self,context):
        self.context=context
        self.page=context.page
        self.page.set_default_timeout(20000)
        self.faker:Faker=self.context.faker


        self.name_input=self.page.locator("[data-qa='signup-name']")
        self.email_input=self.page.locator("[data-qa='signup-email']")
        self.signup_button=self.page.locator("[data-qa='signup-button']")


        self.title_gender_radio=self.page.locator("//input[@type='radio' and @id='id_gender1']")
        self.password_input=self.page.locator("[data-qa='password']")

        self.date_of_birth_days_select=self.page.locator("[data-qa='days']")
        self.date_of_birth_month_select=self.page.locator("[data-qa='months']")
        self.date_of_birth_years_select=self.page.locator("[data-qa='years']")

        self.first_name_input=self.page.locator("[data-qa='first_name']")
        self.last_name_input=self.page.locator("[data-qa='last_name']")

        self.address_input=self.page.locator("[data-qa='address']")
        self.address2_input=self.page.locator("[data-qa='address2']")

        self.country_select=self.page.locator("[data-qa='country']")
        self.state_input=self.page.locator("[data-qa='state']")
        self.city_input=self.page.locator("[data-qa='city']")
        self.zipcode_input=self.page.locator("[data-qa='zipcode']")
        self.mobile_number_input=self.page.locator("[data-qa='mobile_number']")

        self.create_account_button=self.page.locator("[data-qa='create-account']")



    def fill_firtsname(self,nombre=None):
        if nombre is None:
            self.name_input.fill(self.faker.first_name())
        else:
            self.name_input.fill(nombre)


    def fill_email(self,correo=None):
        if correo is None:
            self.email_input.fill(self.faker.email())
        else:
            self.email_input.fill(correo)

    def click_signup_button(self):
        self.signup_button.click()

    def fill_formulary(self):
        self.title_gender_radio.click()
        self.password_input.fill("123456789")
        self.date_of_birth_days_select.select_option(index=2)
        self.date_of_birth_month_select.select_option(index=2)
        self.date_of_birth_years_select.select_option(index=2)
        self.first_name_input.fill(self.faker.first_name())
        self.last_name_input.fill(self.faker.last_name())
        self.address_input.fill(self.faker.address())
        self.address2_input.fill(self.faker.secondary_address())
        self.country_select.select_option(index=1)
        self.state_input.fill(self.faker.state())
        self.city_input.fill(self.faker.city())
        self.zipcode_input.fill(self.faker.zipcode())
        self.mobile_number_input.fill("+12125550123")
    def click_create_account_button(self):
        self.create_account_button.click()

    def verify_text_in_page(self,text):
        assert self.page.locator(f"text={text}"),f"NO SE ENCONTRO EL TEXTO {text}"

