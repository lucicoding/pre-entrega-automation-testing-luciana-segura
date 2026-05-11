# Automation QA - SauceDemo

## Popósito del proyecto
Este proyecto tiene como objetivo automatizar flujos básicos de navegación web utilizando Selenium WebDriver y Python sobre el sitio de pruebas https://www.saucedemo.com/.

Las pruebas utilizadas verifican funcionalidades como login, visualización de productos, la presencia de distintos elementos en la interfaz y operaciones básicas del carrito de compras.

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Git 
- GitHub

## Instrucciones de instalación de dependencias
Ejecutar en terminal:
- pip install selenium pytest pytest-html

## Comandos para ejecutar pruebas
Ejecutar todos los tests:
- pytest -v

Ejecutar un archivo específico:
- pytest tests/nombre_de_archivo.py -v

Ejemplos:
- Test login: pytest tests/test_login.py -v
- Test inventario: pytest tests/test_inventory.py -v
- Test carrito: pytest tests/test_carrito.py -v

Generar reporte HTML
- pytest -v --html=reports/reporte.html