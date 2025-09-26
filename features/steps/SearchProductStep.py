from behave import *

from pages.CartPage import CartPage
from pages.SearchProductPage import SearchProductPage


@step("El usuario busca el producto {texto}")
def step_impl(context, texto):
    search_product_page:SearchProductPage=context.search_product_page
    search_product_page.fill_search(texto)
    search_product_page.click_search_button()

@then("El usuario deberia visualizar varios productos")
def step_impl2(context):
    search_product_page:SearchProductPage=context.search_product_page
    search_product_page.verify_products()


@step("El usuario agrega todos los productos al carrrito de compras")
def step_impl3(context):
    search_product_page:SearchProductPage=context.search_product_page
    cart_page:CartPage=context.cart_page
    products_id=search_product_page.get_all_products_id()

    for i in products_id:
        cart_page.add_product_in_cart(i)
        cart_page.click_continue_shopping_button()


@then("El usuario debería visualizar cada producto agregado")
def step_impl4(context):
    search_product_page:SearchProductPage=context.search_product_page
    cart_page:CartPage=context.cart_page

    products_id=search_product_page.get_all_products_id()
    for i in products_id:
        cart_page.verify_product_index_in_page(i)

