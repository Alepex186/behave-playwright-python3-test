from playwright.sync_api import TimeoutError as PlaywrightTimeoutError,expect   


class BasePage:
    def __init__(self, context):
        self.context = context
        self.page = context.page
        self.page.set_default_timeout(20000)

    # --- Métodos de carga de página ---

    def wait_for_page_load(self):
        """Espera a que la página esté 100% cargada (DOM + recursos de red)."""
        self.page.wait_for_load_state("load")
        self.page.wait_for_load_state("networkidle")

    # --- Métodos de navegación ---

    def navigate_to(self, url):
        """Navega a una URL y espera a que esté completamente cargada."""
        self.page.goto(url, wait_until="networkidle")
        self.wait_for_page_load()

    # --- Métodos de interacción ---

    def click_element(self, locator):
        """Hace click en un elemento usando su selector."""
        self.page.locator(locator).click()

    def fill_input(self, locator, text):
        """Rellena un campo de texto usando su selector."""
        self.page.locator(locator).fill(text)

    def select_option(self, locator, **kwargs):
        """Selecciona una opción de un dropdown usando su selector."""
        self.page.locator(locator).select_option(**kwargs)

    def get_text(self, locator):
        """Obtiene el texto de un elemento usando su selector."""
        return self.page.locator(locator).text_content()

    def get_input_value(self, locator):
        """Obtiene el valor de un input usando su selector."""
        return self.page.locator(locator).input_value()

    # --- Métodos de scroll ---

    def scroll_to_element(self, locator):
        """Hace scroll hasta un elemento usando su selector."""
        self.page.locator(locator).scroll_into_view_if_needed()

    # --- Métodos de espera ---

    def wait_for_element_detached(self, selector):
        """Espera a que un elemento desaparezca del DOM."""
        self.page.wait_for_selector(selector, state="detached")

    # --- Métodos de verificación ---

    def verify_text_in_page(self, text):
        """Verifica que un texto exista en la página."""
        locator = self.page.get_by_text(text)
        expect(locator).not_to_have_count(0)

    def verify_url_contains(self, text):
        """Verifica que la URL actual contenga un texto."""
        assert text in self.page.url, f"La URL no contiene: {text}"

    def verify_element_count(self, locator, min_count=1):
        """Verifica que existan al menos min_count elementos con el selector."""
        count = self.page.locator(locator).count()
        assert count >= min_count, f"Se esperaban al menos {min_count} elementos, se encontraron {count}"

    # --- Métodos de retry ---

    def click_with_retry(self, locator, max_attempts=10, wait_time=1000):
        """Intenta hacer click en un elemento con reintentos en caso de error 520."""
        for attempt in range(1, max_attempts + 1):
            try:
                response = self.page.goto(self.page.url, wait_until="networkidle")
                self.wait_for_page_load()

                if response and response.status == 520:
                    raise Exception("Error 520 detectado")

                self.page.locator(locator).click(timeout=wait_time * 1000)
                return

            except PlaywrightTimeoutError as e:
                print(f"Timeout en intento {attempt}: {e}")

            except Exception as e:
                if "520" in str(e):
                    print(f"Error 520 detectado en intento {attempt}, recargando...")
                else:
                    print(f"Error inesperado: {e}")
                    raise

            self.page.reload()
            self.wait_for_page_load()
            self.page.wait_for_timeout(wait_time * 1000)

        raise Exception(f"No se pudo clicar en {locator} después de {max_attempts} intentos")