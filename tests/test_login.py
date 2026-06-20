import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.data_reader import leer_csv
from utils.logger import logger
@pytest.mark.parametrize("user,password, resultado", leer_csv("data/login_data.csv"))
def test_login_multiple(driver,user,password,resultado):
    logger.info("Inicio del test de login")
    login= LoginPage(driver)
    inventory= InventoryPage(driver)
    login.abrir_pagina()
    logger.info(f"Intentando login con usuario: {user}")
    login.hacer_login(user, password)
    if resultado=="ok":
            logger.info("Login esperado exitoso")
            assert inventory.login_exitoso()
    else:
            logger.error("Login esperado fallido")
            assert inventory.error_visible()
    

