# Automation QA - SauceDemo

## Popósito del proyecto
Este proyecto tiene como objetivo la creación de un framework de automatización de pruebas desarollado en Python utilizando Pytest, Selenium WebDriver y Requests. Incluye pruebas de UI para el sito SauceDemo y pruebas de API para JSONPlaceholder. 
Las pruebas utilizadas verifican funcionalidades como login, logout, visualización de productos, la presencia de distintos elementos en la interfaz, correcta función del filtro y operaciones básicas del carrito de compras.

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Requests
- pytest-html
- Git 
- GitHub

## Estructura del proyecto
- proyecto-final-automation-testing-luciana-segura/
- data/
        login_data.csv
- pages/
        cart_page.py
        inventory_page.py
        login_page.py
- reports/
        screenshots/
        reporte.html
- tests/
        test_api.py
        test_carrito.py
        test_inventory.py
        test_login.py
        test_logout.py
        test_orden.py
- utils/
        _init_.py
        data_reader.py
        logger.py
- conftest.py
- README.md


## Instrucciones de instalación de dependencias
Ejecutar en terminal:
- pip install selenium 
- pip install pytest 
- pip install pytest-html 
- pip install requests

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

## Cómo intrpretar los reportes
El reporte HTML se genera en la carpeta reports. Al abrir reporte.html se pude visualizar:
- Tests ejecutados.
- Estado (Passed/Failed).
- Duración de cada prueba.
- Detalle de errores en caso de fallo.
- Capturas de pantalla asociadas a pruebas fallidas.

