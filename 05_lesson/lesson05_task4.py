from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

un = "input[name='username']"
push_login = driver.find_element(By.CSS_SELECTOR, un)
push_login.send_keys("tomsmith")

pw = "input[id='password']"
push_pass = driver.find_element(By.CSS_SELECTOR, pw)
push_pass.send_keys("SuperSecretPassword!")

sleep(2)

push_log = "button.radius"
push_log = driver.find_element(By.CSS_SELECTOR, push_log)
push_log.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.flash.success')))

text = element.text
print(text)

sleep(10)

driver.quit()

