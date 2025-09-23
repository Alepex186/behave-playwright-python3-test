from behave import *

from pages.HomePage import HomePage
from pages.TestCasesPage import TestCasesPage


@when("El usuario navega a la página de TestCases")
def step_impl(context):
    home_page:HomePage=context.home_page
    home_page.click_test_cases()


@then('El usuario deberia visualizar el mensaje "Test Cases"')
def step_impl2(context):
    test_cases:TestCasesPage=context.test_cases_page
    mensaje_a_verificar="Test Cases"
    test_cases.verify_text_in_page(mensaje_a_verificar)