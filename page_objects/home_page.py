from .base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def click_accessories_button(self):
        self.click_element(By.CSS_SELECTOR, "[aria-controls='accessories']")

    def click_view_all(self):
        self.click_element(By.CSS_SELECTOR, "#accessories")