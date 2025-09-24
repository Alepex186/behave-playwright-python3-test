
from behave import *

from pages.HomePage import HomePage
from pages.ProductsPage import ProductsPage


@Given("El usuario está en la pagina Products")
def step_impl(context):
    home_page:HomePage=context.home_page
    home_page.goto()
    home_page.click_products()


@step("El usuario accede a los detalles del primer producto")
def step_impl2(context):
    products_page:ProductsPage=context.products_page
    products_page.click_item_view_product(1)

@then("El usuario deberia visualiza los detalles del producto")
def step_impl3(context):
    products_page:ProductsPage=context.products_page
    products_page.verify_view_product()


@when("El usuario navega a la página de Products")
def step_impl4(context):
    home_page:HomePage=context.home_page
    home_page.click_products()