from playwright.sync_api import Page


class CartPage:
    def __init__(self,context):
        self.page:Page=context.page

    def add_product_in_cart(self, index):
        product_add_to_cart=self.page.locator(f"a[data-product-id='{index}']")
        product_add_to_cart.first.click()

    def verify_text_in_page(self, text):
        assert self.page.locator(f"text={text}"),"No se encontro el texto"

    def verify_products_in_page(self):
        products=self.page.locator("tbody tr")
        assert products.count() > 0,"No hay elementos agregado al carrito"

    def click_continue_shopping_button(self):
        shopping_button=self.page.locator("div.modal-footer button")
        shopping_button.click()