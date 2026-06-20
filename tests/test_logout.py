import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
def test_logout():
    driver=webdriver.Chrome()
    login= LoginPage(driver)
    inventory= InventoryPage(driver)
    login.abrir_pagina()
    login.hacer_login("standard_user", "secret_sauce")
    inventory.abrir_menu()
    inventory.hacer_logout()
    assert driver.current_url=="https://www.saucedemo.com/"