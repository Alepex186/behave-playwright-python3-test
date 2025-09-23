# Created by Desktop-NG250 at 21/9/2025
Feature: Suscripción en la página

  Scenario: Suscribirse correctamente en la página principal
    Given El usuario está en la página principal
    When El usuario hace scroll hacia el footer
    And El usuario ingresa su correo test123@gmail.com en el campo de Subscription
    And El usuario envia el formulario de Subscription
    Then El usuario debería visualizar el mensaje "You have been successfully subscribed!"


  Scenario: Suscribirse correctamente en la página Cart
    Given El usuario está en la página de Cart
    When El usuario ingresa su correo test123@gmail.com en el campo de Subscription
    And El usuario envia el formulario de Subscription
    Then El usuario debería visualizar el mensaje "You have been successfully subscribed!"
