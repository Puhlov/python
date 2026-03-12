import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

class CartPage(Page):
    """
    Представляет страницу корзины.
    """
    def __init__(self, driver):
        """
        Инициализация CartPage.

        Args:
            driver: Экземпляр Selenium WebDriver.
        """
        super().__init__(driver)
        self.checkout_button = (By.ID, "checkout")
        self.cart_contents = (By.CLASS_NAME, "cart_item")

    @allure.step("Нажатие кнопки 'Checkout'")
    def click_checkout(self):
        """
        Нажимает кнопку оформления заказа.
        """
        self.driver.find_element(*self.checkout_button).click()

    @allure.step("Получение списка элементов товаров в корзине")
    def get_cart_items(self) -> list:
        """
        Возвращает список всех элементов товаров, находящихся в корзине.

        Returns:
            Список WebElement'ов, представляющих товары в корзине.
        """
        return self.driver.find_elements(*self.cart_contents)