import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

class CheckoutPage(Page):
    """
    Представляет страницу оформления заказа.
    """
    def __init__(self, driver):
        """
        Инициализация CheckoutPage.

        Args:
            driver: Экземпляр Selenium WebDriver.
        """
        super().__init__(driver)
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.postal_code_input = (By.NAME, "postalCode")
        self.continue_button = (By.XPATH, "//input[@value='Continue']")
        self.total_price = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнение информации: Имя: {first_name}, Фамилия: {last_name}, Индекс: {postal_code}")
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполняет поля информации для оформления заказа.

        Args:
            first_name: Строка с именем.
            last_name: Строка с фамилией.
            postal_code: Строка с почтовым индексом.
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    @allure.step("Нажатие кнопки 'Continue'")
    def click_continue(self):
        """
        Нажимает кнопку "Continue".
        """
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получение итоговой цены")
    def get_total_price(self) -> str:
        """
        Возвращает текст элемента с итоговой ценой.

        Returns:
            Строка, представляющая итоговую цену.
        """
        return self.driver.find_element(*self.total_price).text