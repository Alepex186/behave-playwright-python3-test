# Created by Desktop-NG250 at 19/9/2025
Feature: verificar productos
  # Enter feature description here

  Scenario: Verificar detalles del primer producto
    Given El usuario está en la pagina Products
    When El usuario accede a los detalles del primer producto
    Then El usuario deberia visualiza los detalles del producto