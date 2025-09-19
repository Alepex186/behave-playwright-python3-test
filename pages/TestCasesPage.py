from playwright.sync_api import Page


class TestCasesPage:
    def __init__(self,context):
        self.page:Page=context.page
        self.page.set_default_timeout(40000)

    def verify_text_in_page(self, mensaje_a_verificar):
        assert self.page.locator(f"text={mensaje_a_verificar}").is_visible(),f"No se ha encontrado el mensaje {mensaje_a_verificar}"


