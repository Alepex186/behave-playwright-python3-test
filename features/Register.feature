# Created by Desktop-NG250 at 17/9/2025
Feature: Registrarse en la pagina web


  Scenario: Registrarse con datos válidos
    Given El usuario esta en la sección de registro en la página Signup / Login
    When El usuario ingresa un nombre y correo válidos en el formulario inicial de registro
    And El usuario envía el formulario inicial de registro
    And El usuario es redirigido al formulario principal de registro
    And El usuario completa el formulario principal de registro con datos válidos
    And El usuario envía el formulario principal de registro
    Then El usuario debería visualizar el mensaje "Account Created!"


  Scenario Outline: Registrarse con email existente
    Given El usuario esta en la sección de registro en la página Signup / Login
    When El usuario ingresa su nombre <nombre> y el correo <correo> en el formulario inicial de registro
    And El usuario envía el formulario inicial de registro
    Then El usuario deberia visualizar el mensaje "Email Address already exist!"

  Examples:
    |nombre|correo|
    |Test  |test0987123@gmail.com |