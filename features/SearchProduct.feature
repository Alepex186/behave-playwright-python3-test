# Created by Desktop-NG250 at 21/9/2025
@SearchProduct
Feature: Búsqueda de productos en el sitio
  Como usuario del sistema de compras
  Quiero buscar productos escribiendo palabras clave en el campo de búsqueda
  Para encontrar fácilmente artículos relacionados y agregarlos al carrito
  Y confirmar que se mantengan después de iniciar sesión con mis credenciales


  Scenario Outline: Búsqueda exitosa de productos
    Given El usuario está en la pagina Products
    And El usuario busca el producto <producto>
    Then El usuario deberia visualizar varios productos

  Examples:
    |producto|
    |Women|
    |Men  |
    |Kids |

  Scenario Outline: Buscar productos y verificar el carrito después de iniciar sesión
    Given El usuario está en la pagina Products
    When El usuario busca el producto <producto>
    And El usuario agrega todos los productos al carrrito de compras
    And El usuario navega a la página de Cart
    Then El usuario debería visualizar cada producto agregado
    And El usuario inicia sesión con las credenciales <correo_valido> <contraseña>
    And El usuario navega a la página de Cart
    And El usuario debería visualizar cada producto agregado

    Examples:
    |producto|correo_valido        |contraseña  |
    |Women   |test0987123@gmail.com|123456      |
    |Men     |test0987123@gmail.com|123456      |
    |Kids    |test0987123@gmail.com|123456      |