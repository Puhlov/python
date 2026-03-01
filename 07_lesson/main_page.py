from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver  
        self.add_backpack_button = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.add_tshirt_button = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie_button = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_items_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_backpack_button)
        ).click()
        self.driver.find_element(*self.add_tshirt_button).click()
        self.driver.find_element(*self.add_onesie_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()