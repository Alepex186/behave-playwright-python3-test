from pages.BasePage import BasePage


class TestCasesPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores ---
        self.TITLE_HEADING = "h2.title.text-center b"

    def verify_text_in_element(self, mensaje_a_verificar):
        """Sobrescribe para verificar texto exacto en el heading de la página."""
        message = self.get_text(self.TITLE_HEADING)
        assert message == mensaje_a_verificar, f"No se ha encontrado el mensaje {mensaje_a_verificar}"
