import re
from playwright.sync_api import Page


class CategoryProductsPage:
    def __init__(self,context):
        self.page:Page=context.page
        self.accordian_section=self.page.locator("div#accordian")
        self.category_section=None

    def click_category_button(self, categoria):
        self.category_section=self.accordian_section.locator("div.panel.panel-default",has_text=categoria)

        category_button = self.page.locator("a[data-parent='#accordian']",has_text=re.compile(r"\s*" + re.escape(categoria) + r"\s*"))
        category_button.click()

    def click_sub_category_button(self, subcategoria):
        sub_category_button=self.category_section.locator("a[href^='/category_products/']",has_text=re.compile(r"\s*" + re.escape(subcategoria) + r"\s*"))
        sub_category_button.click()


    def verify_text_in_page(self, text):
        assert self.page.locator(f"text={text}"),"No se encontro el texto"
