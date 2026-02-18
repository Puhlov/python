from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
    # Открытие сайта
driver.get("https://www.saucedemo.com/")
    # Авторизация
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce") # Пароль по умолчанию для стандартного пользователя
login_button.click()
    # Добавление товаров в корзину
add_backpack_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_tshirt_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
add_onesie_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
add_backpack_button.click()
add_tshirt_button.click()
add_onesie_button.click()

    # Переход в корзину
cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_link.click()
    # Нажатие Checkout
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

    # Заполнение формы
first_name_field = driver.find_element(By.ID, "first-name")
last_name_field = driver.find_element(By.ID, "last-name")
postal_code_field = driver.find_element(By.ID, "postal-code")
first_name_field.send_keys("Тестовое")
last_name_field.send_keys("Имя")
postal_code_field.send_keys("12345")

    # Нажатие Continue

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

    # Получение итоговой стоимости

total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
total_text = total_element.text

total_element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
)
total_text = total_element.text    
    
    # Проверка итоговой суммы

expected_total = "$58.29"
if total_text == expected_total:
    print(f"Итоговая сумма ({total_text}) соответствует ожидаемой.")
else:
    print(f"Итоговая сумма ({total_text}) не соответствует ожидаемой ({expected_total}).")


driver.quit()

            