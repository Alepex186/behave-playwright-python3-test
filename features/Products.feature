# Created by Desktop-NG250 at 19/9/2025
Feature: verificar productos
  # Enter feature description here

  Scenario: Verificar detalles del primer producto
    Given El usuario está en la pagina Products
    When El usuario accede a los detalles del primer producto
    Then El usuario deberia visualiza los detalles del producto


  Scenario Outline: Enviar reseña de producto
    Given El usuario está en la pagina Products
    When El usuario accede a los detalles del primer producto
    And El usuario rellena el formulario de reseña con los datos <nombre> <correo> <descripción>
    And El usuario envia el formulario de reseña
    Then El usuario deberia visualizar el mensaje "Thank you for your review."

    Examples:
      |nombre|correo               |descripción       |
      |test  |test0987123@gmail.com|Buen producto     |