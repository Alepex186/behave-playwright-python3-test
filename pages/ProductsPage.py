from pages.BasePage import BasePage


class ProductsPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores: Detalle de producto ---
        self.PRODUCT_NAME = "div.product-information h2"
        self.PRODUCT_CATEGORY = "div.product-information p"
        self.PRODUCT_PRICE = "div.product-information span span"
        self.PRODUCT_AVAILABILITY = "div.product-information p"
        self.PRODUCT_CONDITION = "div.product-information p"
        self.PRODUCT_BRAND = "div.product-information p"

        # --- Selectores: Formulario de reseña ---
        self.REVIEW_NAME_INPUT = "input#name"
        self.REVIEW_EMAIL_INPUT = "input#email"
        self.REVIEW_TEXTAREA = "textarea#review"
        self.REVIEW_SUBMIT_BUTTON = "button#button-review"

    def click_item_view_product(self, index_product):
        self.click_element(f"[href='/product_details/{index_product}']")

    def verify_view_product(self):
        product_name_text = self.page.locator(self.PRODUCT_NAME)
        product_category = self.page.locator(self.PRODUCT_CATEGORY, has_text="Category:")
        product_price = self.page.locator(self.PRODUCT_PRICE, has_text="Rs.")
        product_availability = self.page.locator(self.PRODUCT_AVAILABILITY, has_text="Availability:")
        product_condition = self.page.locator(self.PRODUCT_CONDITION, has_text="Condition:")
        product_brand = self.page.locator(self.PRODUCT_BRAND, has_text="Brand:")

        assert len(product_name_text.text_content()) > 2
        assert len(product_category.text_content().split(":")[1]) > 2
        assert len(product_price.text_content().strip().split(".")[1]) > 2
        assert "In Stock" in product_availability.text_content()
        assert "New" in product_condition.text_content()
        assert len(product_brand.text_content().split(":")[1]) > 2

    def fill_review(self, nombre, correo, descripcion):
        self.fill_input(self.REVIEW_NAME_INPUT, nombre)
        self.fill_input(self.REVIEW_EMAIL_INPUT, correo)
        self.fill_input(self.REVIEW_TEXTAREA, descripcion)

    def send_review_formulary(self):
        self.click_element(self.REVIEW_SUBMIT_BUTTON)
