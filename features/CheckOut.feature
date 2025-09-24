# Created by Desktop-NG250 at 24/9/2025
@CheckOut
Feature: Verificar funcionalidad de pago
  Como usuario, quiero completar el proceso de pago de manera segura y eficiente,
  para poder adquirir los productos de mi carrito de compras.

  Scenario: Intentar comprar sin una cuenta
    Given El usuario está en la pagina Products
    When El usuario agrega un producto al carrito y cierra la ventana emergente
    And El usuario navega a la página de Cart
    And El usuario procede a pagar
    Then El usuario deberia visualizar el mensaje "Register / Login account to proceed on checkout."

  Scenario: Completar compra registrándose en el proceso de checkout
    Given El usuario está en la página principal
    And El usuario esta en la pagina de login / registro
    When El usuario registra una nueva cuenta
    And El usuario navega a la página de Products
    And El usuario agrega un producto al carrito y cierra la ventana emergente
    And El usuario navega a la página de Cart
    And El usuario procede a pagar
    Then El usuario debería visualizar sus datos de dirección
    And El usuario confirma la orden
    And El usuario completa el formulario de pago con los datos
    |nombre_tarjeta|numero_tarjeta|CVC |mes_expiración|año_expiración|
    |Test          |1234567890    |233 |09            |2030          |
    And El usuario envia el formulario de pago
    And El usuario deberia visualizar el mensaje "Congratulations! Your order has been confirmed!"

