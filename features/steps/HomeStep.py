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
