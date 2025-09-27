from behave import *

from pages.CartPage import CartPage
from pages.HomePage import HomePage


@when("El usuario navega a la sección recommended items")
def step_impl(context):
    home_page:HomePage=context.home_page
    home_page.scroll_to_recommended_items()



@step("El usuario agrega un producto al carrito desde la sessión recommended items")
def step_impl2(context):
    home_page:HomePage=context.home_page
    cart_page:CartPage=context.cart_page

    home_page.add_product_in_cart(4)
    cart_page.click_continue_shopping_button()


@step("El usuario borra la cuenta")
def step_impl3(context):
    home_page:HomePage=context.home_page
    home_page.delete_account()


@step('El usuario deberia visualizar el mensaje "Account Deleted!"')
def step_impl4(context):
    home_page:HomePage=context.home_page
    mensaje="Account Deleted!"
    home_page.verify_text_in_page(mensaje)