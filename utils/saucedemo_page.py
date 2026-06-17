from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SauceDemoPage:
    def __init__(self, driver):
        self.driver= driver
    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")
    def escribir_usuario(self, user):
         self.driver.find_element(By.ID,"user-name").send_keys(user)
    def escribir_password(self):
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
    def login_exitoso(self):
         return "inventory" in self.driver.current_url 
    def error_visible(self):
         return "error" in self.driver.page_source
    def obtener_titulo(self):
         return self.driver.title
    def hay_productos(self):
         productos= self.driver.find_elements(By.CLASS_NAME, "inventory_item")
         return len(productos)>0
    def menu_visible(self):
         return self.driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    def filtro_visible(self):
         return self.driver.find_element(By.CLASS_NAME,"product_sort_container").is_displayed()
    def agregar_primer_producto(self):
         botones= self.driver.find_elements(By.CLASS_NAME,"btn_inventory")
         botones[0].click()
    def obtener_contador_carrito(self):
         return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    def abrir_carrito(self):
         self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    def producto_en_carrito(self):
         productos= self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
         return len(productos)>0
    def obtener_nombre_primer_producto(self):
         return self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")[0].text
    def obtener_precio_primer_producto(self):
         return self.driver.find_elements(By.CLASS_NAME,"inventory_item_price")[0].text
    def nombre_producto_carrito(self):
         return self.driver.find_element(By.CLASS_NAME,"inventory_item_name").text
