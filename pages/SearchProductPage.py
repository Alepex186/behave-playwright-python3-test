from pages.BasePage import BasePage


class SearchProductPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores ---
        self.SEARCH_INPUT = "input[id='search_product']"
        self.SEARCH_BUTTON = "button[id='submit_search']"
        self.PRODUCTS_GRID = "div.features_items div.col-sm-4"
        self.PRODUCT_ID_LINKS = "a[data-product-id]"

    def fill_search(self, texto):
        self.fill_input(self.SEARCH_INPUT, texto)

    def click_search_button(self):
        self.click_element(self.SEARCH_BUTTON)

    def verify_products(self):
        self.verify_element_count(self.PRODUCTS_GRID, min_count=1)

    def get_all_products_id(self):
        products_index_list = []
        products = self.page.locator(self.PRODUCTS_GRID)
        products_index = products.locator(self.PRODUCT_ID_LINKS)

        for i in range(products_index.count()):
            product_id = products_index.nth(i).get_attribute("data-product-id")
            products_index_list.append(product_id)

        products_index_list = list(dict.fromkeys(products_index_list))
        return products_index_list
