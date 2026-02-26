from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver  
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, "#result")
        self.button_7 = (By.CSS_SELECTOR, "#number7")
        self.button_plus = (By.CSS_SELECTOR, "#operator_add")
        self.button_8 = (By.CSS_SELECTOR, "#number8")
        self.button_equals = (By.CSS_SELECTOR, "#operator_equals")

    def enter_delay(self, delay):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.delay_input)
        ).send_keys(delay)

    def click_button_7(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_7)
        ).click()

    def click_button_plus(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_plus)
        ).click()

    def click_button_8(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_8)
        ).click()

    def click_button_equals(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_equals)
        ).click()

    def get_result(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.result_display)
        ).text