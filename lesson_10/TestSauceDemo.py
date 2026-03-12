import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

@allure.feature("Процесс покупки")
class TestSauceDemo(unittest.TestCase):
    """
    Набор тестов для функционала покупки на сайте SauceDemo.
    """

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """
        Фикстура для настройки и очистки WebDriver перед каждым тестом.
        """
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @allure.title("Успешное оформление заказа")
    @allure.description("Тест проверяет полный процесс покупки: вход, добавление товаров, оформление заказа и проверку цены.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_process(self):
        """
        Тест проверяет сценарий успешного оформления заказа.
        """
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        main_page = MainPage(self.driver)
        main_page.add_product_to_cart(0)
        main_page.add_product_to_cart(1)
        main_page.add_product_to_cart(2)
        main_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.click_continue()

        with allure.step("Проверка итоговой цены"):
            total_price = checkout_page.get_total_price()
            print("Total Price:", total_price)
            self.assertEqual(total_price, "Total: $58.29", "Итоговая цена не совпадает с ожидаемой.")

if __name__ == "__main__":
    unittest.main()