from behave import *

from pages.ContactUsPage import ContactUsPage
from pages.HomePage import HomePage



@Given("El usuario está en la página de Contact us")
def step_impl(context):
    home_page:HomePage=context.home_page
    home_page.goto()
    home_page.click_contact_us()

@step("El usuario rellena el formulario de Contact us con")
def step_impl2(context):
    datos=context.table
    datos=datos[0]
    nombre=datos[0]
    correo=datos[1]
    asunto=datos[2]
    mensaje=datos[3]

    contact_us_page:ContactUsPage=context.contact_us_page
    contact_us_page.fill_formulary(nombre,correo,asunto,mensaje)




@step("El usuario envía el formulario de Contact us")
def step_impl3(context):
    contact_us_page:ContactUsPage=context.contact_us_page
    contact_us_page.click_submit()

@then('El usuario debería visualizar el mensaje "Success! Your details have been submitted successfully."')
def step_impl4(context):
    contact_us_page: ContactUsPage = context.contact_us_page
    text="Success! Your details have been submitted successfully."
    contact_us_page.verify_text_in_page(text)