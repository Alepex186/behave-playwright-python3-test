
from playwright.sync_api import Page


class SearchProductPage:
    def __init__(self,context):
        self.page:Page=context.page

    def fill_search(self, texto):
        search_product_input=self.page.locator("input[id='search_product']")
        search_product_input.fill(texto)

    def click_search_button(self):
        search_product_button=self.page.locator("button[id='submit_search']")
        search_product_button.click()

    def verify_products(self):
        products=self.page.locator("div.features_items div.col-sm-4")
        assert products.count() > 0,"No se encontraron elementos"
