import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

class MainPage(Page):
    """
    Представляет главную страницу с товарами.
    """
    def __init__(self, driver):
        """
        Инициализация MainPage.

        Args:
            driver: Экземпляр Selenium WebDriver.
        """
        super().__init__(driver)
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавление товара с индексом {product_index} в корзину")
    def add_product_to_cart(self, product_index: int):
        """
        Добавляет товар в корзину по его индексу.

        Args:
            product_index: Целое число, индекс товара (начиная с 0).
        """
        self.driver.find_elements(*self.add_to_cart_buttons)[product_index].click()

    @allure.step("Переход к странице корзины")
    def go_to_cart(self):
        """
        Нажимает кнопку корзины для перехода к ней.
        """
        self.driver.find_element(*self.cart_button).click()