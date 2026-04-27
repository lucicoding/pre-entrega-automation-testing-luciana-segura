import pytest
from selenium import webdriver
from pages.saucedemo_page import SauceDemoPage
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
    page.hacer_login(user)
    if resultado:
        assert page.login_exitoso()
    else:
        assert page.error_visible()

