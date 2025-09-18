import time

from behave import *

from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage


@when("El usuario ingresa su nombre en el apartado de New User Signup!")
def step_impl2(context):
    register_page:RegisterPage=context.register_page
    register_page.fill_firtsname()

@step("El usuario ingresa su correo en el apartado de New User Signup!")
def step_impl3(context):
    register_page:RegisterPage=context.register_page
    register_page.fill_email()

@step("El usuario hace click en el boton Signup")
def step_impl4(context):
    register_page:RegisterPage=context.register_page
    register_page.click_signup_button()

@step("El usuario rellena el formulario de registro")
def step_impl5(context):
    register_page:RegisterPage=context.register_page
    register_page.fill_formulary()

@step("El usuario hace click en el boton Create Account")
def step_impl6(context):
    register_page:RegisterPage=context.register_page
    register_page.click_create_account_button()

@then("El usuario deberia visualizar el mensaje Account Created!")
def step_impl7(context):
    register_page: RegisterPage = context.register_page
    register_page.verify_text_in_page("Account Created!")


@step("El usuario ingresa el correo {correo} en el apartado de New User Signup!")
def step_impl8(context,correo):
    register_page:RegisterPage=context.register_page
    register_page.fill_email(correo)


@then("El usuario deberia visualizar el mensaje Email Address already exist!")
def step_impl9(context):
    register_page:RegisterPage=context.register_page
    time.sleep(3)
    register_page.verify_text_in_page("Email Address already exist!")