Feature: Iniciar sessión en la pagina web


  Scenario: Iniciar sesión con credenciales válidas
    Given El usuario esta en la pagina principal
    And El usuario hace click en el boton Registrarse / Iniciar sesión
    When El usuario ingresa su correo test0987123@gmail.com en el login
    And El usuario ingresa su contraseña 123456 en el login
    And El usuario hace click en el boton login
    Then Deberia mostrarse en el header el mensaje Logged in as

  Scenario: Iniciar sesión con credenciales incorrectas
    Given El usuario esta en la pagina principal
    And El usuario hace click en el boton Registrarse / Iniciar sesión
    When El usuario ingresa su correo incorrectemail123123@gmail.com en el login
    And El usuario ingresa su contraseña 123456 en el login
    And El usuario hace click en el boton login
    Then Deberia mostrarse en el mensaje Your email or password is incorrect!

