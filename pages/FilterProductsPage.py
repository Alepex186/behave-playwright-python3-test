import re

from playwright.sync_api import Page


class FilterProductsPage:
    def __init__(self,context):
        self.page:Page=context.page
        self.accordian_section=self.page.locator("div#accordian")
        self.category_section=None

    def click_category_button(self, tipo):
        self.category_section=self.accordian_section.locator("div.panel.panel-default",has_text=tipo)

        category_button = self.page.locator("a[data-parent='#accordian']",has_text=re.compile(r"\s*" + re.escape(tipo) + r"\s*"))
        category_button.click()

    def click_sub_category_button(self, valor):
        sub_category_button=self.category_section.locator("a[href^='/category_products/']",has_text=re.compile(r"\s*" + re.escape(valor) + r"\s*"))
        sub_category_button.click()


    def verify_text_in_page(self, text):
        locator = self.page.locator(f"text='{text}'")
        assert locator.count() > 0, f"No se encontró el texto: {text}"

    def click_brand_button(self, brand):
        brand_button=self.page.locator("a[href^='/brand_products/']",has_text=re.compile(r"\s*" + re.escape(brand) + r"\s*"))
        brand_button.click()