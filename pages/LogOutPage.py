from playwright.sync_api import Page


class LogOutPage:
    def __init__(self,context):
        self.page:Page = context.page
        self.page.set_default_timeout(20000)
        self.log_out_button=self.page.locator("//li//a[@href='/logout']")

    def click_log_out_button(self):
        self.log_out_button.click()

    def verify_log_out(self):
        assert self.page.url.endswith("/login"), "ERROR AL CERRAR SESION"



