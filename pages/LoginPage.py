class LoginPage:
    def __init__(self,context):
        self.context=context
        self.page=context.page
        self.page.set_default_timeout(20000)
        self.email_input=self.page.locator('[data-qa="login-email"]')
        self.password_input=self.page.locator('[data-qa="login-password"]')
        self.login_button=self.page.locator('[data-qa="login-button"]')

    def fill_email(self,email):
        self.email_input.fill(email)

    def fill_password(self,password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def full_login(self,email,password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_page(self,mensaje:str):
        assert self.page.locator(f"text={mensaje}").is_visible(),"ERROR AL VERIFICAR"