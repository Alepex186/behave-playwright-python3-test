class HomePage:
    def __init__(self,context):
        self.context=context
        self.page=context.page
        self.page.set_default_timeout(20000)
        self.signup_login_button=self.page.locator("//li//a[@href='/login']")
        self.contact_us_button=self.page.locator("//li//a[@href='/contact_us']")


    def goto(self):
        self.page.goto(self.context.HOME_PAGE_URL)

    def click_signup_login(self):
        self.signup_login_button.click()

    def click_contact_us(self):
        self.contact_us_button.click()
