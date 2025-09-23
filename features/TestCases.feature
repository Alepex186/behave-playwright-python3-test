# Created by Desktop-NG250 at 18/9/2025
Feature: Verificar la página de casos de pruebas
  Scenario: Verificar que carga correctamente la página
    Given El usuario está en la página principal
    When El usuario navega a la página de TestCases
    Then El usuario deberia visualizar el mensaje "Test Cases"