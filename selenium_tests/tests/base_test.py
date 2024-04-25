import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://watermark.pinta.pro/prestashop16/en/")
        self.driver.implicitly_wait(4)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
