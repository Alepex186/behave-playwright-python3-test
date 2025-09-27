from playwright.sync_api import Page


class HomePage:
    def __init__(self,context):
        self.context=context
        self.page:Page=context.page
        self.page.set_default_timeout(20000)
        self.signup_login_button=self.page.locator("//li//a[@href='/login']")
        self.contact_us_button=self.page.locator("//li//a[@href='/contact_us']")
        self.test_cases_button=self.page.locator("//li//a[@href='/test_cases']")
        self.products_button=self.page.locator("//li//a[@href='/products']")
        self.footer=self.page.locator("footer")
        self.cart_button=self.page.locator("//li//a[@href='/view_cart']")
        self.section_recommended_items=self.page.locator("div.recommended_items")



    def goto(self):
        self.page.goto(self.context.HOME_PAGE_URL)

    def click_signup_login(self):
        self.signup_login_button.click()

    def click_contact_us(self):
        self.contact_us_button.click()

    def click_test_cases(self):
        self.test_cases_button.click()

    def click_products(self):
        self.products_button.click()

    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()

    def click_cart(self):
        self.cart_button.click()

    def scroll_to_recommended_items(self):
        self.section_recommended_items.scroll_into_view_if_needed()

    def add_product_in_cart(self, index):
        product_add_to_cart=self.section_recommended_items.locator(f"a[data-product-id='{index}']")
        product_add_to_cart.first.click()

    def delete_account(self):
        delete_account_button=self.page.locator("a[href='/delete_account']")
        delete_account_button.click()

    def verify_text_in_page(self, text):
        locator = self.page.locator(f"text={text}")
        assert locator.count() > 0, f"No se encontró el texto: {text}"