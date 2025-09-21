from playwright.sync_api import Page


class TestCasesPage:
    def __init__(self,context):
        self.page:Page=context.page
        self.page.set_default_timeout(40000)

    def verify_text_in_page(self, mensaje_a_verificar):
        message=self.page.locator("h2.title.text-center b")
        assert message.text_content() == mensaje_a_verificar,f"No se ha encontrado el mensaje {mensaje_a_verificar}"


