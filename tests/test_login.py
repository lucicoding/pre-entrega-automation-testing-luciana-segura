import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
from utils.data_reader import leer_csv
@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.mark.parametrize("user,password, resultado", leer_csv("data/login_data.csv"))
def test_login_multiple(driver,user,password,resultado):
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    print("Pagina SauceDemo abierta")
    page.hacer_login(user, password)
    try:
        if resultado=="ok":
            assert page.login_exitoso()
            print("Login de {user} realizado correctamente")
        else:
            assert page.error_visible()
            print("Mensaje de error mostrado correctamente")
    except:
        driver.save_screenshot("reports/screenshots/error_login_{user}.png")
        raise

