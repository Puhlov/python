import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    edge_driver_path = r"C:\Users\puhlo\OneDrive\Desktop\edge\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_submission(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'firstName')))
    form_data = {
        "firstName": "Иван",
        "lastName": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone": "+7985899998787",
        "zip": "",
        "city": "Москва",
        "country": "Россия",
        "jobPosition": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        driver.find_element(By.NAME, field_name).send_keys(value)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_field = driver.find_element(By.NAME, "zip")
    assert "error" in zip_code_field.get_attribute("class"), "Поле Zip code не подсвечено красным"

    fields = driver.find_elements(By.CSS_SELECTOR, "input")
    for field in fields:
        if field != zip_code_field:
            assert "success" in field.get_attribute("class"), f"Поле {field.get_attribute('name')} не подсвечено зеленым"

