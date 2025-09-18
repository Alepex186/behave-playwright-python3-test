# Created by Desktop-NG250 at 17/9/2025
Feature: Cerrar sesión en la pagina web

  Scenario: Cerrar sesión correctamente
    Given El usuario esta logueado con las credenciales test0987123@gmail.com 123456
    When El usuario hace click en el boton LogOut
    Then El usuario deberia ser redirigido a la pagina de Registrarse / Iniciar sesión