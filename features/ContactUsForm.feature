# Created by Desktop-NG250 at 17/9/2025
Feature: Formulario Contact Us Form

  Scenario: Enviar formulario
    Given El usuario está en la página de Contact us
    When El usuario rellena el formulario de Contact us con
      | nombre | correo               | asunto   | mensaje           |
      | Test   | test123123@gmail.com | Soporte  | Tengo un problema |
    And El usuario envía el formulario de Contact us
    Then El usuario debería visualizar el mensaje "Success! Your details have been submitted successfully."

