from selenium.webdriver.common.by import By
class CartPage:
    def __init__(self, driver):
        self.driver= driver
    def producto_en_carrito(self):
         productos= self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
         return len(productos)>0
    def nombre_producto_carrito(self):
         return self.driver.find_element(By.CLASS_NAME,"inventory_item_name").text