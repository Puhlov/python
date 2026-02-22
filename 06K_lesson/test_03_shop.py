import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_saucedemo_shopping_cart(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Имя")
    driver.find_element(By.ID, "last-name").send_keys("Фамилия")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    total_price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_price = total_price_element.text

    assert total_price == "$58.29", f"Ожидаемая сумма $58.29, получено {total_price}"