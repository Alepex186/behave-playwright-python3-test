from behave import *

from pages.FilterProductsPage import FilterProductsPage


@when('El usuario selecciona la categoria {categoria} y la subcategoria {subcategoria}')
def step_impl(context, categoria, subcategoria):
    filter_products_page:FilterProductsPage=context.filter_products_page
    filter_products_page.click_category_button(categoria)
    filter_products_page.click_sub_category_button(subcategoria)


@then('El usuario debería ver el título de la página como "{tipo} - {valor} Products"')
def step_impl2(context, tipo, valor):
    filter_products_page:FilterProductsPage=context.filter_products_page
    filter_products_page.verify_text_in_page(f"{tipo} - {valor} Products")


@when("El usuario selecciona la marca {brand}")
def step_impl3(context, brand):
    filter_products_page:FilterProductsPage=context.filter_products_page
    filter_products_page.click_brand_button(brand)
