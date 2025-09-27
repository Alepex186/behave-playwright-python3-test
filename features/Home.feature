Feature: Verificar funcionalidad de productos recomendados
  Como usuario del sistema de compras
  Quiero poder interactuar con la sección de productos recomendados
  Para agregar artículos fácilmente al carrito y confirmar que se muestran correctamente en la página de carrito

  Scenario: Verificar que productos recomendados funcionen como deben
    Given El usuario está en la página principal
    When El usuario navega a la sección recommended items
    And El usuario agrega un producto al carrito desde la sessión recommended items
    And El usuario navega a la página de Cart
    Then El usuario debería visualizar los productos agregados
