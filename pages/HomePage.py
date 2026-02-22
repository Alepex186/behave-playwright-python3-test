from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores ---
        self.SIGNUP_LOGIN_BUTTON = "//li//a[@href='/login']"
        self.CONTACT_US_BUTTON = "//li//a[@href='/contact_us']"
        self.TEST_CASES_BUTTON = "//li//a[@href='/test_cases']"
        self.PRODUCTS_BUTTON = "//li//a[@href='/products']"
        self.CART_BUTTON = "//li//a[@href='/view_cart']"
        self.FOOTER = "footer"
        self.SECTION_RECOMMENDED_ITEMS = "div.recommended_items"
        self.DELETE_ACCOUNT_BUTTON = "a[href='/delete_account']"

    def goto(self):
        self.navigate_to(self.context.HOME_PAGE_URL)

    def click_signup_login(self):
        self.click_with_retry(self.SIGNUP_LOGIN_BUTTON)

    def click_contact_us(self):
        self.click_with_retry(self.CONTACT_US_BUTTON)

    def click_test_cases(self):
        self.click_with_retry(self.TEST_CASES_BUTTON)

    def click_products(self):
        self.click_with_retry(self.PRODUCTS_BUTTON)

    def click_cart(self):
        self.click_with_retry(self.CART_BUTTON)

    def scroll_to_footer(self):
        self.scroll_to_element(self.FOOTER)

    def scroll_to_recommended_items(self):
        self.scroll_to_element(self.SECTION_RECOMMENDED_ITEMS)

    def add_product_in_cart(self, index):
        recommended = self.page.locator(self.SECTION_RECOMMENDED_ITEMS)
        product_add_to_cart = recommended.locator(f"a[data-product-id='{index}']")
        product_add_to_cart.first.click()

    def delete_account(self):
        self.click_element(self.DELETE_ACCOUNT_BUTTON)
