from behave import *

from pages.LogOutPage import LogOutPage


@when("El usuario hace click en el boton LogOut")
def step_impl(context):
    log_out_page:LogOutPage=context.log_out_page
    log_out_page.click_log_out_button()


@then("El usuario deberia ser redirigido a la pagina de Registrarse / Iniciar sesión")
def step_impl2(context):
    log_out_page:LogOutPage=context.log_out_page
    log_out_page.verify_log_out()