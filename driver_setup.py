# driver_setup.py
from selenium import webdriver

class DriverSetup:
    def setup_driver(self):
        # Configure the driver setup here
        self.driver = webdriver.Chrome()
        return self.driver

    def teardown_driver(self, driver):
        driver.quit()