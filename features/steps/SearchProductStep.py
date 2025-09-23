from behave import *

from pages.SearchProductPage import SearchProductPage


@step("El usuario busca el producto {texto}")
def step_impl(context, texto):
    search_product_page:SearchProductPage=context.search_product_page
    search_product_page.fill_search(texto)
    search_product_page.click_search_button()

@then("El usuario deberia visualizar varios productos")
def step_impl3(context):
    search_product_page:SearchProductPage=context.search_product_page
    search_product_page.verify_products()


@when("El usuario navega a la página de Products")
def step_impl(context):
    raise NotImplementedError(u'STEP: When El usuario navega a la página de Products')