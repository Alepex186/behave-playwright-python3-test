# Created by Desktop-NG250 at 17/9/2025
Feature: Registrarse en la pagina web

  Scenario: Registrarse con datos validos
    Given El usuario esta en la pagina principal
    And El usuario hace click en el boton Registrarse / Iniciar sesión
    When El usuario ingresa su nombre en el apartado de New User Signup!
    And El usuario ingresa su correo en el apartado de New User Signup!
    And El usuario hace click en el boton Signup
    And El usuario rellena el formulario de registro
    And El usuario hace click en el boton Create Account
    Then El usuario deberia visualizar el mensaje Account Created!

  Scenario: Registrarse con email existente
    Given El usuario esta en la pagina principal
    And El usuario hace click en el boton Registrarse / Iniciar sesión
    When El usuario ingresa su nombre en el apartado de New User Signup!
    And El usuario ingresa el correo test0987123@gmail.com en el apartado de New User Signup!
    And El usuario hace click en el boton Signup
    Then El usuario deberia visualizar el mensaje Email Address already exist!
