# Created by Desktop-NG250 at 24/9/2025
Feature: Verificar la funcionalidad de filtrado en la página de productos
  Como usuario del sistema de compras
  Quiero poder filtrar los productos por categorías y marcas
  Para encontrar fácilmente los artículos que me interesan

  Scenario Outline: Verificar buscar por categoria
    Given El usuario está en la pagina Products
    When El usuario selecciona la categoria <categoria> y la subcategoria <subcategoria>
    Then El usuario debería ver el título de la página como "<categoria> - <subcategoria> Products"

  
    Examples:
      | categoria | subcategoria |
      | Women     | Dress        |
      | Women     | Tops         |
      | Women     | Saree        |
      | Men       | Tshirts      |
      | Men       | Jeans        |
      | Kids      | Dress        |
      | Kids      | Tops & Shirts|


  Scenario Outline: Verificar buscar por marcas
    Given El usuario está en la pagina Products
    When El usuario selecciona la marca <brand>
    Then El usuario debería ver el título de la página como "Brand - <brand> Products"

  Examples:
    |brand              |
    |Polo               |
    |H&M                |
    |Madame             |
    |Mast & Harbour     |
    |Babyhug            |
    |Allen Solly Junior |
    |Kookie Kids        |
    |Biba               |
