from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")
print("Страница успешно загружена")

try: 

    button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")

    button.click()

    print("Синяя кнопка успешно нажата")
except Exception as e:
    print(f"Произошла ошибка: {e}")
sleep(60)
