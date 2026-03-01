import pytest  
from selenium import webdriver  
from login_page import LoginPage  
from main_page import MainPage  
from cart_page import CartPage  
from checkout_page import CheckoutPage

@pytest.fixture  
def driver():
    driver = webdriver.Firefox()
    yield driver  
    driver.quit()

def test_shopping_cart(driver):
    # Открываем сайт магазина  
    driver.get("https://www.saucedemo.com/")
    
    # Авторизация  
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    # Добавление товаров в корзину  
    main_page = MainPage(driver)
    main_page.add_items_to_cart()
    
    # Переход в корзину  
    main_page.go_to_cart()
    
    # Нажатие кнопки Checkout  
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()
    
    # Заполнение формы данными  
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("John", "Doe", "12345")
    
    # Чтение итоговой стоимости  
    total = checkout_page.get_total()
    
    # Закрытие браузера и проверка итоговой суммы  
    assert total == "Total: $58.29"