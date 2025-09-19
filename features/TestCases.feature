# Created by Desktop-NG250 at 18/9/2025
Feature: Verificar la pagina de casos de pruebas
  Scenario: Verificar que carga correctamente la pagina
    Given El usuario esta en la pagina principal
    When El usuario hace click en el boton Test Cases
    Then El usuario deberia visualizar el mensaje Test Cases