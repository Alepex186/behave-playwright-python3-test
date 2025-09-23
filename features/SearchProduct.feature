# Created by Desktop-NG250 at 21/9/2025
Feature: Búsqueda de productos en el sitio
  # Enter feature description here

  Scenario: Búsqueda exitosa de productos
    Given El usuario está en la pagina Products
    And El usuario busca el producto "Women"
    Then El usuario deberia visualizar varios productos