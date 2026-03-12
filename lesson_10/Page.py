import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

class Page:
    """
    Базовый класс для всех страниц веб-приложения.
    Предоставляет общий интерфейс для взаимодействия с WebDriver.
    """
    def __init__(self, driver):
        """
        Инициализация базового класса страницы.

        Args:
            driver: Экземпляр Selenium WebDriver.
        """
        self.driver = driver