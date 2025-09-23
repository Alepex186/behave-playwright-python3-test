from behave import *

from pages.HomePage import HomePage
from pages.SubscriptionPage import SubscriptionPage


@when("El usuario hace scroll hacia el footer")
def step_impl(context):
    home_page:HomePage=context.home_page
    home_page.scroll_to_footer()


@step("El usuario ingresa su correo {correo} en el campo de Subscription")
def step_impl2(context,correo):
    subscription_page:SubscriptionPage=context.subscription_page
    subscription_page.fill_email(correo)

@step("El usuario envia el formulario de Subscription")
def step_impl3(context):
    subscription_page:SubscriptionPage=context.subscription_page
    subscription_page.click_send_subscription()

@then('El usuario debería visualizar el mensaje "You have been successfully subscribed!"')
def step_impl4(context):
    subscription_page:SubscriptionPage=context.subscription_page
    mensaje="You have been successfully subscribed!"
    subscription_page.verify_text_in_page(mensaje)

@step("El usuario navega a la página de Cart")
def step_impl5(context):
    home_page:HomePage=context.home_page
    home_page.click_cart()


@given("El usuario está en la página de Cart")
def step_impl6(context):
    home_page:HomePage=context.home_page
    home_page.goto()
    home_page.click_cart()