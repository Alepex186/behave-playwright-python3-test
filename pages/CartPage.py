from playwright.sync_api import Page


class CartPage:
    def __init__(self,context):
        self.page:Page=context.page
        self.quantity_product_before=0
        self.quantity_product_after=0

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

    def verify_quantity_product_in_cart(self, cantidad):
        product=self.page.locator("tbody tr").first
        quantity=product.locator("td.cart_quantity button").text_content()
        assert str(quantity) == str(cantidad)

    def remove_product_in_cart(self, index):
        tbody=self.page.locator("tbody")
        products=tbody.locator("tr")

        self.quantity_product_before=products.count()

        product=tbody.locator(f"tr#product-{index}")
        delete_button = product.locator("td.cart_delete a.cart_quantity_delete")
        delete_button.click()



    def verify_removed_product_in_cart(self,index):
        tbody=self.page.locator("tbody")
        products=tbody.locator("tr")
        self.page.wait_for_selector(f"tr#product-{index}",state="detached")
        self.quantity_product_after=products.count()


        assert int(self.quantity_product_before)-1 == self.quantity_product_after


