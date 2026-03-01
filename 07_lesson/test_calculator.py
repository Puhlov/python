import pytest  
from selenium import webdriver  
from calculator_page import CalculatorPage  # Импортируйте ваш класс

@pytest.fixture  
def driver():
    # Настройки WebDriver для Chrome  
    driver = webdriver.Chrome()
    yield driver  
    driver.quit()

def test_calculator(driver):
    # Открываем страницу калькулятора  
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    calculator_page = CalculatorPage(driver)

    # Ввод значения задержки  
    calculator_page.set_delay("45")
    
    # Выполнение вычисления  
    calculator_page.click_button7()
    calculator_page.click_button_plus()
    calculator_page.click_button8()
    calculator_page.click_button_equals()
    
    # Проверка результата  
    result = calculator_page.get_result()
    
    # Ожидаем, что результат будет 15  
    assert result == "15"