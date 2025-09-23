Feature: Iniciar sessión en la pagina web


  Scenario Outline: Iniciar sesión con credenciales válidas
    Given El usuario esta en la sección de login en la página Signup / Login
    When El usuario ingresa su correo <correo_valido> en el login
    And El usuario ingresa su contraseña <contraseña> en el login
    And El usuario envía el formulario de login
    Then Deberia mostrarse en el header el mensaje "Logged in as"

    Examples:
      |correo_valido        |contraseña|
      |test0987123@gmail.com|123456    |


  Scenario Outline: Iniciar sesión con credenciales incorrectas
    Given El usuario esta en la sección de login en la página Signup / Login
    When El usuario ingresa su correo <correo_invalido> en el login
    And El usuario ingresa su contraseña <contraseña> en el login
    And El usuario envía el formulario de login
    Then Deberia mostrarse en el mensaje "Your email or password is incorrect!"

  Examples:
    |correo_invalido               |contraseña|
    |incorrectemail123123@gmail.com|123456    |