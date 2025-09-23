from behave import *

from pages import HomePage
from pages.RegisterPage import RegisterPage




@Given("El usuario esta en la sección de registro en la página Signup / Login")
def click_boton_registro(context):
    home_page:HomePage=context.home_page
    home_page.goto()
    home_page.click_signup_login()


@when("El usuario ingresa un nombre y correo válidos en el formulario inicial de registro")
def step_impl2(context):
    register_page:RegisterPage=context.register_page
    register_page.fill_firtsname()
    register_page.fill_email()

@step("El usuario envía el formulario inicial de registro")
def step_impl(context):
    register_page:RegisterPage=context.register_page
    register_page.click_signup_button()


@step("El usuario es redirigido al formulario principal de registro")
def step_impl2(context):
    register_page:RegisterPage=context.register_page
    register_page.verify_text_in_page("Enter Account Information")

@step("El usuario completa el formulario principal de registro con datos válidos")
def step_impl3(context):
    register_page:RegisterPage=context.register_page
    register_page.fill_formulary()


@step("El usuario envía el formulario principal de registro")
def step_impl4(context):
    register_page:RegisterPage=context.register_page
    register_page.click_create_account_button()

@then('El usuario debería visualizar el mensaje "Account Created!"')
def step_impl5(context):
    register_page:RegisterPage=context.register_page
    register_page.verify_text_in_page("Account Created!")


@then('El usuario deberia visualizar el mensaje "Email Address already exist!"')
def step_impl6(context):
    register_page:RegisterPage=context.register_page
    register_page.verify_text_in_page("Email Address already exist!")


@when("El usuario ingresa su nombre {nombre} y el correo {correo} en el formulario inicial de registro")
def step_impl(context,nombre,correo):
    register_page:RegisterPage=context.register_page
    register_page.fill_firtsname(nombre)
    register_page.fill_email(correo)
