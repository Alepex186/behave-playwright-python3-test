import time

from behave import *

from pages.HomePage import HomePage
from pages.ProductsPage import ProductsPage


@Given("El usuario está en la pagina Products")
def step_impl(context):
    home_page:HomePage=context.home_page
    home_page.goto()
    home_page.click_products()


@step("El usuario accede a los detalles del primer producto")
def step_impl2(context):
    products_page:ProductsPage=context.products_page
    products_page.click_item_view_product(1)

@then("El usuario deberia visualiza los detalles del producto")
def step_impl3(context):
    products_page:ProductsPage=context.products_page
    products_page.verify_view_product()


@when("El usuario navega a la página de Products")
def step_impl4(context):
    home_page:HomePage=context.home_page
    home_page.click_products()


@step("El usuario rellena el formulario de reseña con los datos {nombre} {correo} {descripcion}")
def step_impl5(context, nombre, correo, descripcion):
    products_page:ProductsPage=context.products_page
    products_page.fill_review(nombre,correo,descripcion)


@step("El usuario envia el formulario de reseña")
def step_impl6(context):
    products_page:ProductsPage=context.products_page
    products_page.send_review_formulary()

@then('El usuario deberia visualizar el mensaje "Thank you for your review."')
def step_impl7(context):
    products_page:ProductsPage=context.products_page
    mensaje="Thank you for your review."
    products_page.verify_text_in_page(mensaje)