from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores ---
        self.EMAIL_INPUT = '[data-qa="login-email"]'
        self.PASSWORD_INPUT = '[data-qa="login-password"]'
        self.LOGIN_BUTTON = '[data-qa="login-button"]'

    def fill_email(self, email):
        self.fill_input(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.fill_input(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def full_login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()