from behave import *

from pages.SearchProductPage import SearchProductPage


@step("El usuario ingresa el texto {texto} en el input con el placeholder Search Product")
def step_impl(context, texto):
    search_product_page:SearchProductPage=context.search_product_page
    search_product_page.fill_search(texto)

@step("El usuario hace click en el boton con imagen de lupa")
def step_impl2(context):
    search_product_page:SearchProductPage=context.search_product_page
    search_product_page.click_search_button()

@then("El usuario deberia visualizar varios productos")
def step_impl3(context):
    search_product_page:SearchProductPage=context.search_product_page
    search_product_page.verify_products()