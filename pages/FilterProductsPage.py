import re

from pages.BasePage import BasePage


class FilterProductsPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        # --- Selectores ---
        self.ACCORDIAN_SECTION = "div#accordian"
        self.CATEGORY_LINK = "a[data-parent='#accordian']"
        self.SUB_CATEGORY_LINK = "a[href^='/category_products/']"
        self.BRAND_LINK = "a[href^='/brand_products/']"

        # --- Estado ---
        self.category_section = None

    def click_category_button(self, tipo):
        self.category_section = self.page.locator(self.ACCORDIAN_SECTION).locator(
            "div.panel.panel-default", has_text=tipo
        )
        category_button = self.page.locator(
            self.CATEGORY_LINK,
            has_text=re.compile(r"\s*" + re.escape(tipo) + r"\s*")
        )
        category_button.click()

    def click_sub_category_button(self, valor):
        sub_category_button = self.category_section.locator(
            self.SUB_CATEGORY_LINK,
            has_text=re.compile(r"\s*" + re.escape(valor) + r"\s*")
        )
        sub_category_button.click()

    def click_brand_button(self, brand):
        brand_button = self.page.locator(
            self.BRAND_LINK,
            has_text=re.compile(r"\s*" + re.escape(brand) + r"\s*")
        )
        brand_button.click()
