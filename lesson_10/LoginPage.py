import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

class LoginPage(Page):
    """
    Представляет страницу входа в систему.
    """
    def __init__(self, driver):
        """
        Инициализация LoginPage.

        Args:
            driver: Экземпляр Selenium WebDriver.
        """
        super().__init__(driver)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Ввод логина: {username}")
    def enter_username(self, username: str):
        """
        Вводит логин в поле ввода имени пользователя.

        Args:
            username: Строка с логином.
        """
        self.driver.find_element(*self.username_input).send_keys(username)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str):
        """
        Вводит пароль в поле ввода пароля.

        Args:
            password: Строка с паролем.
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    @allure.step("Нажатие кнопки 'Login'")
    def click_login(self):
        """
        Нажимает кнопку входа.
        """
        self.driver.find_element(*self.login_button).click()