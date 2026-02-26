from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver  
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.postal_code_input = (By.NAME, "postalCode")
        self.continue_button = (By.XPATH, "//input[@value='Continue']")
        self.total_price = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text