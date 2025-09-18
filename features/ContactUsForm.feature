# Created by Desktop-NG250 at 17/9/2025
Feature: Formulario Contact Us Form

  Scenario: Enviar formulario
    Given El usuario esta en la pagina principal
    When El usuario hace click en el boton Contact us
    And El usuario rellena el formulario de Contact us con
      | nombre | correo               | asunto   | mensaje           |
      | Test   | test123123@gmail.com | Soporte  | Tengo un problema |
    And El usuario hace click en el boton Submit del apartado Contact us
    And El usuario hace click en aceptar en el dialogo
    Then El usuario deberia visualizar el mensaje Success! Your details have been submitted successfully.

