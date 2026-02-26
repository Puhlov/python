import unittest  
from selenium import webdriver  
from login_page import LoginPage  
from main_page import MainPage  
from cart_page import CartPage  
from checkout_page import CheckoutPage

class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        main_page = MainPage(self.driver)
        main_page.add_product_to_cart(0)  # Sauce Labs Backpack  
        main_page.add_product_to_cart(1)  # Sauce Labs Bolt T-Shirt  
        main_page.add_product_to_cart(2)  # Sauce Labs Onesie  
        main_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.click_continue()

        total_price = checkout_page.get_total_price()
        print("Total Price:", total_price)
        self.assertEqual(total_price, "Total: $58.29")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()