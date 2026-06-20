import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

def test_agregar_producto_carrito():
    driver=webdriver.Chrome()
    login= LoginPage(driver)
    cart= CartPage(driver)
    inventory= InventoryPage(driver)
    login.abrir_pagina()
    login.hacer_login("standard_user", "secret_sauce")
    print("Login realizado correctamente")
    nombre_producto= inventory.obtener_nombre_primer_producto()
    inventory.agregar_primer_producto()
    print("Producto agregado al carrito")
    assert inventory.obtener_contador_carrito()=="1"
    print("Contador del carrito actualizado correctamente")
    inventory.abrir_carrito()
    print("Carrito abierto correctamente")
    assert cart.producto_en_carrito()
    assert cart.nombre_producto_carrito()==nombre_producto
    print("Producto visible en carrito")
    driver.quit()
def test_falla(driver):
    driver.get("https://www.saucedemo.com/")
    assert False
     