from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver  
        self.first_name_input = (By.CSS_SELECTOR, "#first-name")
        self.last_name_input = (By.CSS_SELECTOR, "#last-name")
        self.zip_code_input = (By.CSS_SELECTOR, "#postal-code")
        self.finish_button = (By.CSS_SELECTOR, "#finish")
        self.total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_checkout_form(self, first_name, last_name, zip_code):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.finish_button).click()

    def get_total(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        )
        return self.driver.find_element(*self.total_label).text