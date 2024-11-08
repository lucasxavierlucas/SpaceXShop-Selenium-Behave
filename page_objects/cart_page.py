# cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage

class CartPage(BasePage):
    def get_total_price(self):
        total_price_element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "[data-cart-total='']"))
        )
        return total_price_element.text