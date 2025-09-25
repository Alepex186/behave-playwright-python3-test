from behave import *

from pages.CategoryProductsPage import CategoryProductsPage


@when('El usuario selecciona la categoria {categoria} y la subcategoria {subcategoria}')
def step_impl(context, categoria, subcategoria):
    category_products_page:CategoryProductsPage=context.category_products_page
    category_products_page.click_category_button(categoria)
    category_products_page.click_sub_category_button(subcategoria)


@then('El usuario debería ver el título de la página como "{categoria} - {subcategoria} Products"')
def step_impl(context, categoria, subcategoria):
    category_products_page:CategoryProductsPage=context.category_products_page
    category_products_page.verify_text_in_page(f"{categoria} - {subcategoria} Products")