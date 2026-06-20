import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
from utils.login_page import LoginPage
from utils.cart_page import CartPage
from utils.inventory_page import InventoryPage
def test_pagina_inventario():
    driver=webdriver.Chrome()
    login= LoginPage(driver)
    inventory= InventoryPage(driver)
    login.abrir_pagina()
    login.hacer_login("standard_user", "secret_sauce")
    print("Ingreso exitoso a inventario")
    assert "Swag Labs" in inventory.obtener_titulo()
    assert inventory.hay_productos()
    print("Productos visibles correctamente")
    nombre_producto= inventory.obtener_nombre_primer_producto()
    precio_producto= inventory.obtener_precio_primer_producto()
    print(nombre_producto)
    print(precio_producto)
    assert nombre_producto!=""
    assert "$" in precio_producto
    assert inventory.menu_visible()
    assert inventory.filtro_visible()
    print("Menu y filtros visibles")
    