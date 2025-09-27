from behave import *

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@Given("El usuario está en la página principal")
def pagina_principal(context):
    context.home_page.goto()

@Given("El usuario esta en la sección de login en la página Signup / Login")
def click_boton_iniciar_session(context):
    home_page:HomePage=context.home_page
    home_page.goto()
    home_page.click_signup_login()

@When("El usuario ingresa su correo {correo} en el login")
def ingresar_correo(context,correo):
    login_page:LoginPage=context.login_page
    login_page.fill_email(correo)

@When("El usuario ingresa su contraseña {contrasenia} en el login")
def ingresar_contrasenia(context,contrasenia):
    login_page:LoginPage=context.login_page
    login_page.fill_password(contrasenia)

@When("El usuario envía el formulario de login")
def click_boton_login(context):
    login_page:LoginPage=context.login_page
    login_page.click_login()

@Then('Deberia mostrarse en el header el mensaje "Logged in as"')
def verificar_mensaje_correcto(context):
    mensaje_correcto='Logged in as'
    login_page:LoginPage=context.login_page
    login_page.verify_text_in_page(mensaje_correcto)

@then('Deberia mostrarse en el mensaje "Your email or password is incorrect!"')
def verificar_mensaje_incorrecto(context):
    mensaje_incorrecto= "Your email or password is incorrect!"
    login_page:LoginPage=context.login_page
    login_page.verify_text_in_page(mensaje_incorrecto)


@given("El usuario esta logueado con las credenciales {correo} {contrasenia}")
def iniciar_sesion_completo(context,correo,contrasenia):
    home_page:HomePage=context.home_page
    home_page.goto()
    home_page.click_signup_login()
    login_page:LoginPage=context.login_page
    login_page.fill_email(correo)
    login_page.fill_password(contrasenia)
    login_page.click_login()

@step("El usuario inicia sesión con las credenciales {correo} {contrasenia}")
def iniciar_sesion_completo(context,correo,contrasenia):
    home_page:HomePage=context.home_page
    home_page.goto()
    home_page.click_signup_login()
    login_page:LoginPage=context.login_page
    login_page.fill_email(correo)
    login_page.fill_password(contrasenia)
    login_page.click_login()


@given("El usuario esta en la pagina de login / registro")
def step_impl(context):
    home_page:HomePage=context.home_page
    home_page.click_signup_login()