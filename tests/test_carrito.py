import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
def test_agregar_producto_carrito():
    driver=webdriver.Chrome()
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    page.hacer_login("standard_user")
    nombre_producto= page.obtener_nombre_primer_producto()
    page.agregar_primer_producto()
    assert page.obtener_contador_carrito()=="1"
    page.abrir_carrito()
    assert page.producto_en_carrito()
    assert page.nombre_producto_carrito()==nombre_producto
    driver.quit()
    