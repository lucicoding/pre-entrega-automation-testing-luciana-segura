import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
def test_pagina_inventario():
    driver=webdriver.Chrome()
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    page.hacer_login("standard_user")
    print("Ingreso exitoso a inventario")
    assert "Swag Labs" in page.obtener_titulo()
    assert page.hay_productos()
    print("Productos visibles correctamente")
    nombre_producto= page.obtener_nombre_primer_producto()
    precio_producto= page.obtener_precio_primer_producto()
    print(nombre_producto)
    print(precio_producto)
    assert nombre_producto!=""
    assert "$" in precio_producto
    assert page.menu_visible()
    assert page.filtro_visible()
    print("Menu y filtros visibles")
    driver.quit()
    