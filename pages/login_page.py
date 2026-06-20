from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self, driver):
        self.driver= driver
    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")
    def escribir_usuario(self, user):
         self.driver.find_element(By.ID,"user-name").send_keys(user)
    def escribir_password(self, password):
         self.driver.find_element(By.ID,"password").send_keys(password)
    def hacer_click_login(self):
         self.driver.find_element(By.ID,"login-button").click()
    def hacer_login(self,user, password):
         self.escribir_usuario(user)
         self.escribir_password(password)
         self.hacer_click_login()
         try:
          WebDriverWait(self.driver,10).until(EC.url_contains("inventory"))
         except:
              pass