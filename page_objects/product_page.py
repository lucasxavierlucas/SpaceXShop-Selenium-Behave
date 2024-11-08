from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def select_mug(self):
        # Find the mug button by its href and ensure it's in view before clicking
        mug_button = self.wait_for_element(By.CSS_SELECTOR,
                                           "a[href='/collections/accessories/products/occupy-mars-heat-sensitive-terraforming-mug-new']")
        # Scroll to the element to ensure it's in view
        self.driver.execute_script("arguments[0].scrollIntoView();", mug_button)
        # Click the button once it's in view
        mug_button.click()

    def increase_quantity(self):
        increase_quantity_button = self.wait_for_element(By.CSS_SELECTOR, "[data-action='increase-quantity']")
        increase_quantity_button.click()

    def add_to_cart(self):
        add_to_cart_button = self.wait_for_element(By.CSS_SELECTOR, "[data-action='add-to-cart']")
        add_to_cart_button.click()