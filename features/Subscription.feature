# Created by Desktop-NG250 at 21/9/2025
Feature: Suscripción en la pagina

  Scenario: Suscribirse correctamente en la pagina principal
    Given El usuario esta en la pagina principal
    When El usuario hace scroll hacia el footer
    And El usuario ingresa su correo test123@gmail.com en el campo de Subscription
    And El usuario hace click en el boton con la imagen de una flecha
    Then El usuario deberia visualizar el mensaje You have been successfully subscribed!


  Scenario: Suscribirse correctamente en la pagina Cart
    Given El usuario esta en la pagina principal
    And El usuario hace click en el boton Cart
    When El usuario ingresa su correo test123@gmail.com en el campo de Subscription
    And El usuario hace click en el boton con la imagen de una flecha
    Then El usuario deberia visualizar el mensaje You have been successfully subscribed!