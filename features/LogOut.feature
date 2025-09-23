# Created by Desktop-NG250 at 17/9/2025
Feature: Cerrar sesión en la pagina web

  Scenario Outline: Cerrar sesión correctamente
    Given El usuario esta logueado con las credenciales <correo> <contraseña>
    When El usuario cierra su sesión
    Then El usuario debería ser redirigido a la página Signup / Login

  Examples:
    |correo|contraseña|
    |test0987123@gmail.com|123456|