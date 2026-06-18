import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
def test_agregar_producto_carrito():
    driver=webdriver.Chrome()
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    page.hacer_login("standard_user", "secret_sauce")
    print("Login realizado correctamente")
    nombre_producto= page.obtener_nombre_primer_producto()
    page.agregar_primer_producto()
    print("Producto agregado al carrito")
    assert page.obtener_contador_carrito()=="1"
    print("Contador del carrito actualizado correctamente")
    page.abrir_carrito()
    print("Carrito abierto correctamente")
    assert page.producto_en_carrito()
    assert page.nombre_producto_carrito()==nombre_producto
    print("Producto visible en carrito")
    driver.quit()
    