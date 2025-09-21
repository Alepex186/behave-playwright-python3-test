# Created by Desktop-NG250 at 21/9/2025
Feature: Buscar productos
  # Enter feature description here

  Scenario: Buscar productos correctamente
    Given El usuario esta en la pagina principal
    When El usuario hace click en el boton Products
    And El usuario ingresa el texto Women en el input con el placeholder Search Product
    And El usuario hace click en el boton con imagen de lupa
    Then El usuario deberia visualizar varios productos