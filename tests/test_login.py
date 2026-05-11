import pytest
from selenium import webdriver
from utils.saucedemo_page import SauceDemoPage
@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.mark.parametrize("user, resultado",
 [("standard_user",True),("locked_out_user",False),("problem_user",True),("performance_glitch_user",True),("error_user",True),("visual_user",True)])
def test_login_multiple(driver,user,resultado):
    page= SauceDemoPage(driver)
    page.abrir_pagina()
    print("Pagina SauceDemo abierta")
    page.hacer_login(user)
    try:
        if resultado:
            assert page.login_exitoso()
            print("Login de {user} realizado correctamente")
        else:
            assert page.error_visible()
            print("Mensaje de error mostrado correctamente")
    except:
        driver.save_screenshot("reports/screenshots/error_login_{user}.png")
        raise

