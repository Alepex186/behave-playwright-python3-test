from pages.BasePage import BasePage


class SubscriptionPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores ---
        self.SUBSCRIPTION_EMAIL_INPUT = "input#susbscribe_email"
        self.SUBSCRIPTION_BUTTON = "button#subscribe"

    def fill_email(self, correo):
        self.fill_input(self.SUBSCRIPTION_EMAIL_INPUT, correo)

    def click_send_subscription(self):
        self.click_element(self.SUBSCRIPTION_BUTTON)