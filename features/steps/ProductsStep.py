
from behave import *

from pages.HomePage import HomePage
from pages.ProductsPage import ProductsPage

use_step_matcher("re")


@when("El usuario hace click en el boton Products")
def step_impl(context):
    home_page:HomePage=context.home_page
    home_page.click_products()


@step("El usuario hace click en el boton View Product del primer producto")
def step_impl(context):
    products_page:ProductsPage=context.products_page
    products_page.click_item_view_product(1)

@then("El usuario deberia visualizar el product name, category, price, availability, condition, brand, del producto")
def step_impl(context):
    products_page:ProductsPage=context.products_page
    products_page.verify_view_product()