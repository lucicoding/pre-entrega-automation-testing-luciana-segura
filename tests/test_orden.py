import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
def test_ordenar_productos_z_a():
    driver=webdriver.Chrome()
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    page.hacer_login("standard_user","secret_sauce")
    page.ordenar_z_a()
    nombre_primer_producto= page.obtener_nombre_primer_producto()
    assert nombre_primer_producto=="Test.allTheThings() T-Shirt (Red)"
    