import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
from utils.data_reader import leer_csv
from utils.logger import logger
from datetime import datetime
fecha= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.mark.parametrize("user,password, resultado", leer_csv("data/login_data.csv"))
def test_login_multiple(driver,user,password,resultado):
    logger.info("Inicio del test de login")
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    print("Pagina SauceDemo abierta")
    logger.info(f"Intentando login con usuario: {user}")
    page.hacer_login(user, password)
    try:
        if resultado=="ok":
            logger.info("Login esperado exitoso")
            assert page.login_exitoso()
        else:
            logger.error("Login esperado fallido")
            assert page.error_visible()
    except:
        driver.save_screenshot(f"reports/screenshots/error_login_{user}_{fecha}.png")
        raise

