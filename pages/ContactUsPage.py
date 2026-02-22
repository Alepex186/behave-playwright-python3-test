import time

from pages.BasePage import BasePage


class ContactUsPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores ---
        self.NAME_INPUT = "[data-qa='name']"
        self.EMAIL_INPUT = "[data-qa='email']"
        self.SUBJECT_INPUT = "[data-qa='subject']"
        self.MESSAGE_INPUT = "[data-qa='message']"
        self.SUBMIT_BUTTON = "[data-qa='submit-button']"

    def fill_formulary(self, nombre, correo, asunto, mensaje):
        self.fill_input(self.NAME_INPUT, nombre)
        self.fill_input(self.EMAIL_INPUT, correo)
        self.fill_input(self.SUBJECT_INPUT, asunto)
        self.fill_input(self.MESSAGE_INPUT, mensaje)

    def click_submit(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        time.sleep(1)
        self.click_element(self.SUBMIT_BUTTON)