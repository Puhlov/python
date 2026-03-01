from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver  
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button7 = (By.CSS_SELECTOR, "#c7")
        self.button8 = (By.CSS_SELECTOR, "#c8")
        self.button_plus = (By.CSS_SELECTOR, "#add")
        self.button_equals = (By.CSS_SELECTOR, "#equals")
        self.result_field = (By.CSS_SELECTOR, "#result")

    def set_delay(self, delay):
        delay_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.delay_input)
        )
        delay_element.clear()
        delay_element.send_keys(delay)

    def click_button7(self):
        self.driver.find_element(*self.button7).click()

    def click_button_plus(self):
        self.driver.find_element(*self.button_plus).click()

    def click_button8(self):
        self.driver.find_element(*self.button8).click()

    def click_button_equals(self):
        self.driver.find_element(*self.button_equals).click()

    def get_result(self):
        result_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.result_field)
        )
        return result_element.text