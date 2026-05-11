import pytest
from selenium import webdriver
from pages.saucedemo_page import SauceDemoPage
def test_agregar_producto_carrito():
    driver=webdriver.Chrome()
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    page.hacer_login("standard_user")
    page.agregar_primer_producto()
    assert page.obtener_contador_carrito()=="1"
    page.abrir_carrito()
    assert page.producto_en_carrito()
    driver.quit()
    assert page.nombre_producto_carrito()=="Sauce Labs Backpack"