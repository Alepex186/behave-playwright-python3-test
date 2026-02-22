from pages.BasePage import BasePage


class LogOutPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores ---
        self.LOG_OUT_BUTTON = "//li//a[@href='/logout']"

    def click_log_out_button(self):
        self.click_element(self.LOG_OUT_BUTTON)

    def verify_log_out(self):
        self.verify_url_contains("/login")
