import time

from playwright.sync_api import Page


class ContactUsPage:
    def __init__(self,context):
        self.page:Page=context.page
        self.page.set_default_timeout(20000)
        self.name_input=self.page.locator("[data-qa='name']")
        self.email_input=self.page.locator("[data-qa='email']")
        self.subject_input=self.page.locator("[data-qa='subject']")
        self.message_input=self.page.locator("[data-qa='message']")
        self.submit_button=self.page.locator("[data-qa='submit-button']")

    def fill_formulary(self, nombre, correo, asunto, mensaje):
        self.name_input.fill(nombre)
        self.email_input.fill(correo)
        self.subject_input.fill(asunto)
        self.message_input.fill(mensaje)

    def click_submit(self):
        self.submit_button.click()

    def click_accept_dialog(self):
        self.page.once("dialog",lambda dialog: dialog.accept())

    def verify_text_in_page(self, text):
        assert self.page.locator(f"text={text}"),f"NO SE ENCONTRO EL MENSAJE {text}"

