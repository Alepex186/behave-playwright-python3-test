from behave import *

from pages.CartPage import CartPage
from pages.HomePage import HomePage



@given("El usuario está en la página de Products")
def step_impl(context):
    home_page:HomePage = context.home_page
    home_page.goto()
    home_page.click_products()

@when("El usuario agrega un producto al carrito")
def step_impl2(context):
    cart_page:CartPage=context.cart_page
    cart_page.add_product_in_cart(1)


@then('El usuario debería visualizar el mensaje "Your product has been added to cart."')
def step_impl3(context):
    cart_page:CartPage=context.cart_page
    cart_page.verify_text_in_page("Your product has been added to cart.")
    cart_page.click_continue_shopping_button()

@then("El usuario debería visualizar un producto agregado")
def step_impl4(context):
    cart_page:CartPage=context.cart_page
    cart_page.verify_products_in_page()

@when("El usuario agrega los siguientes productos al carrito de compras:")
def step_impl5(context):
    cart_page:CartPage=context.cart_page
    for index, _ in enumerate(context.table):
        cart_page.add_product_in_cart(index+1)
        cart_page.verify_text_in_page("Your product has been added to cart.")
        cart_page.click_continue_shopping_button()

@then("El usuario debería visualizar los productos agregados")
def step_impl6(context):
    cart_page:CartPage=context.cart_page
    cart_page.verify_products_in_page()

