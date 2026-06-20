import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
from utils.login_page import LoginPage
from utils.cart_page import CartPage
from utils.inventory_page import InventoryPage
def test_ordenar_productos_z_a():
    driver=webdriver.Chrome()
    login= LoginPage(driver)
    inventory= InventoryPage(driver)
    login.abrir_pagina()
    login.hacer_login("standard_user", "secret_sauce")
    inventory.ordenar_z_a()
    nombre_primer_producto= inventory.obtener_nombre_primer_producto()
    assert nombre_primer_producto=="Test.allTheThings() T-Shirt (Red)"
    