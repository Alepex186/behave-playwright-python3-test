# Created by Desktop-NG250 at 19/9/2025
Feature: verificar productos
  # Enter feature description here

  Scenario: Verificar detalles del primer producto
    Given El usuario esta en la pagina principal
    When El usuario hace click en el boton Products
    And El usuario hace click en el boton View Product del primer producto
    Then El usuario deberia visualizar el product name, category, price, availability, condition, brand, del producto