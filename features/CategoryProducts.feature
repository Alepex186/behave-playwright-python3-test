# Created by Desktop-NG250 at 24/9/2025
Feature: Verificar la funcionalidad de filtrado por categoria
  # Enter feature description here

  Scenario Outline: Verificar que la funcionalidad funciones como se espera
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