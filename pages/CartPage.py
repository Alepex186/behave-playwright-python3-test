from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores ---
        self.PRODUCTS_ROWS = "tbody tr"
        self.TBODY = "tbody"
        self.CONTINUE_SHOPPING_BUTTON = "div.modal-footer button"
        self.CART_QUANTITY_BUTTON = "td.cart_quantity button"
        self.CART_DELETE_BUTTON = "td.cart_delete a.cart_quantity_delete"

        # --- Estado ---
        self.quantity_product_before = 0
        self.quantity_product_after = 0

    def add_product_in_cart(self, index):
        product_add_to_cart = self.page.locator(f"a[data-product-id='{index}']")
        product_add_to_cart.first.click()

    def verify_products_in_page(self):
        self.verify_element_count(self.PRODUCTS_ROWS, min_count=1)

    def click_continue_shopping_button(self):
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)

    def verify_quantity_product_in_cart(self, cantidad):
        product = self.page.locator(self.PRODUCTS_ROWS).first
        quantity = product.locator(self.CART_QUANTITY_BUTTON).text_content()
        assert str(quantity) == str(cantidad)

    def remove_product_in_cart(self, index):
        tbody = self.page.locator(self.TBODY)
        products = tbody.locator("tr")
        self.quantity_product_before = products.count()

        product = tbody.locator(f"tr#product-{index}")
        delete_button = product.locator(self.CART_DELETE_BUTTON)
        delete_button.click()

    def verify_removed_product_in_cart(self, index):
        tbody = self.page.locator(self.TBODY)
        products = tbody.locator("tr")
        self.wait_for_element_detached(f"tr#product-{index}")
        self.quantity_product_after = products.count()

        assert int(self.quantity_product_before) - 1 == self.quantity_product_after

    def verify_product_index_in_page(self, index):
        tbody = self.page.locator(self.TBODY)
        product = tbody.locator(f"tr#product-{index}")
        assert product.count() > 0, f"No se encontro el elemento con id: {index}"
