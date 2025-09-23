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




