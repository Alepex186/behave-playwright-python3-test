from playwright.sync_api import Page


class SubscriptionPage:
    def __init__(self,context):
        self.page:Page=context.page
        self.page.set_default_timeout(40000)
        self.subscription_email_input=self.page.locator("input#susbscribe_email")
        self.subscription_button=self.page.locator("button#subscribe")

    def fill_email(self, correo):
        self.subscription_email_input.fill(correo)

    def click_send_subscription(self):
        self.subscription_button.click()

    def verify_text_in_page(self, mensaje):
        assert self.page.locator(f"text={mensaje}").is_visible()
