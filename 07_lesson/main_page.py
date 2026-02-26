from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver  
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_index):
        self.driver.find_elements(*self.add_to_cart_buttons)[product_index].click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()