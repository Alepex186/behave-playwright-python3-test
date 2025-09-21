

from playwright.sync_api import Page


class ProductsPage:
    def __init__(self,context):
        self.page:Page=context.page
        self.page.set_default_timeout(40000)




    def click_item_view_product(self, index_product):
        product=self.page.locator(f"[href='/product_details/{index_product}']")
        product.click()

    def verify_view_product(self):
        product_name_text=self.page.locator("div.product-information h2")
        product_category=self.page.locator("div.product-information p",has_text="Category:")
        product_price=self.page.locator("div.product-information span span",has_text="Rs.")
        product_availability=self.page.locator("div.product-information p",has_text="Availability:")
        product_condition=self.page.locator("div.product-information p",has_text="Condition:")
        product_brand=self.page.locator("div.product-information p",has_text="Brand:")

        assert len(product_name_text.text_content()) > 2
        assert len(product_category.text_content().split(":")[1]) > 2
        assert len(product_price.text_content().strip().split(".")[1]) > 2
        assert "In Stock" in product_availability.text_content()
        assert "New" in product_condition.text_content()
        assert len(product_brand.text_content().split(":")[1]) > 2


