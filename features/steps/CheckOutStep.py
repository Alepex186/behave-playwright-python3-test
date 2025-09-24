from behave import *

from pages.CheckOutPage import CheckOutPage




@step("El usuario procede a pagar")
def step_impl(context):
    check_out_page:CheckOutPage=context.check_out_page
    check_out_page.click_proceed_to_checkout_button()


@then("El usuario debería visualizar sus datos de dirección")
def step_impl2(context):
    check_out_page:CheckOutPage=context.check_out_page
    check_out_page.verify_text_in_page("Address Details")


@step("El usuario confirma la orden")
def step_impl3(context):
    check_out_page:CheckOutPage=context.check_out_page
    check_out_page.click_place_order_button()


@step("El usuario completa el formulario de pago con los datos")
def step_impl4(context):
    table=context.table
    datos=table[0]
    nombre_tarjeta=datos[0]
    numero_tarjeta=datos[1]
    cvc=datos[2]
    mes_expiracion=datos[3]
    anio_expiracion=datos[4]


    check_out_page:CheckOutPage=context.check_out_page
    check_out_page.fill_payment_formulary(nombre_tarjeta,numero_tarjeta,cvc,mes_expiracion,anio_expiracion)


@step("El usuario envia el formulario de pago")
def step_impl5(context):
    check_out_page:CheckOutPage=context.check_out_page
    check_out_page.click_pay_and_confirm_order()

@step('El usuario deberia visualizar el mensaje "Congratulations! Your order has been confirmed!"')
def step_impl6(context):
    check_out_page:CheckOutPage=context.check_out_page
    check_out_page.verify_text_in_page("Congratulations! Your order has been confirmed!")


@then('El usuario deberia visualizar el mensaje "Register / Login account to proceed on checkout."')
def step_impl7(context):
    check_out_page:CheckOutPage=context.check_out_page
    check_out_page.verify_text_in_page("Register / Login account to proceed on checkout.")
