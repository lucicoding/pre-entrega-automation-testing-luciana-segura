from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
class InventoryPage:
    def __init__(self, driver):
        self.driver= driver
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
    def obtener_nombre_primer_producto(self):
         return self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")[0].text
    def obtener_precio_primer_producto(self):
         return self.driver.find_elements(By.CLASS_NAME,"inventory_item_price")[0].text
    def agregar_primer_producto(self):
         botones= self.driver.find_elements(By.CLASS_NAME,"btn_inventory")
         botones[0].click()
    def obtener_contador_carrito(self):
         return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    def abrir_carrito(self):
         self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    def abrir_menu(self):
         self.driver.find_element(By.ID, "react-burger-menu-btn").click()
         WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    def hacer_logout(self):
         logout=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
         logout.click()
    def ordenar_z_a(self):
         Select(
         self.driver.find_element(By.CLASS_NAME,"product_sort_container")
         ).select_by_value("za")
    