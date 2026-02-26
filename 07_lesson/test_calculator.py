import unittest  
from selenium import webdriver  
from calculator_page import CalculatorPage  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def test_calculator_functionality(self):
        calculator_page = CalculatorPage(self.driver)
        
        # Ввод задержки  
        calculator_page.enter_delay("45")
        
        # Нажатие кнопок  
        calculator_page.click_button_7()
        calculator_page.click_button_plus()
        calculator_page.click_button_8()
        calculator_page.click_button_equals()
        
        # Ожидание результата  
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(calculator_page.result_display, "15")
        )
        
        # Проверка результата  
        result = calculator_page.get_result()
        print("Результат:", result)
        self.assertEqual(result, "15")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()