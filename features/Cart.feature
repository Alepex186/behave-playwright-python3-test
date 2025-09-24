# Created by Desktop-NG250 at 21/9/2025
@Cart
Feature: Verificar la funcionalidad del carrito de compras


Scenario: Agregar un producto al carrito de compras
  Given El usuario está en la página de Products
  When El usuario agrega un producto al carrito
  Then El usuario debería visualizar el mensaje "Your product has been added to cart."
  And El usuario navega a la página de Cart
  Then El usuario debería visualizar un producto agregado

Scenario: Agregar dos productos al carrito de compras
  Given El usuario está en la página de Products
  When El usuario agrega los siguientes productos al carrito de compras:
        | producto   |
        | producto 1 |
        | producto 2 |

  And El usuario navega a la página de Cart
  Then El usuario debería visualizar los productos agregados

Scenario Outline: Agregar el mismo producto varias veces al carrito
  Given El usuario está en la pagina Products
  When El usuario agrega el mismo producto <cantidad> veces al carrito
  And El usuario navega a la página de Cart
  Then El usuario debería visualizar los productos agregados
  And El usuario debería visualizar que la cantidad del producto es <cantidad>

  Examples:
  |cantidad|
  |4       |

Scenario: Eliminar producto de carrito
  Given El usuario está en la página de Products
  When El usuario agrega un producto al carrito
  Then El usuario debería visualizar el mensaje "Your product has been added to cart."
  And El usuario navega a la página de Cart
  And El usuario borra un producto del carrito
  And El usuario debería visualizar que disminuye la cantidad de productos en el carrito