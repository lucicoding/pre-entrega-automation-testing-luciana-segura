import pytest
from selenium import webdriver
from pages.saucedemo_page import SauceDemoPage
def test_pagina_inventario():
    driver=webdriver.Chrome()
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    page.hacer_login("standard_user")
    assert "Swag Labs" in page.obtener_titulo()
    assert page.hay_productos()
    assert page.menu_visible()
    assert page.filtro_visible()
    driver.quit()
    