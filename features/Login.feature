Feature: Iniciar sessión en la pagina web

  Scenario: Iniciar sesión con credenciales válidas
    Given El usuario esta en la pagina principal
    And El usuario Hace click en el boton Registrarse / Iniciar sesión
    When El usuario ingresa su correo
    And El usuario ingresa su contraseña
    And El usuario hace click en el boton Acceso
    Then Deberia mostrarse en el header el mensaje Logged in as <test019283>