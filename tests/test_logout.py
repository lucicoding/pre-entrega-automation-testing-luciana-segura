import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
from utils.data_reader import leer_csv
from utils.logger import logger
from datetime import datetime
fecha= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
def test_logout():
    driver=webdriver.Chrome()
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    page.hacer_login("standard_user","secret_sauce")
    page.hacer_logout()
    assert driver.current_url=="https://www.saucedemo.com/"
    driver.quit()