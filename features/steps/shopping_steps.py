from behave import given, when, then
from page_objects.home_page import HomePage
from page_objects.product_page import ProductPage
from page_objects.cart_page import CartPage
from driver_setup import DriverSetup

def before_all(context):
    context.driver_setup = DriverSetup()
    context.driver = context.driver_setup.setup_driver()

@given('I navigate to the SpaceX shop')
def step_given_navigate_to_shop(context):
    context.driver.get("https://shop.spacex.com/")
    context.driver.maximize_window()

@when('I add two "Occupy Mars Mug" to the cart')
def step_when_add_mugs_to_cart(context):
    home_page = HomePage(context.driver)
    home_page.click_accessories_button()
    home_page.click_view_all()

    product_page = ProductPage(context.driver)
    product_page.select_mug()
    product_page.increase_quantity()
    product_page.add_to_cart()

@then('The total cost should be 40.00')
def step_then_validate_total_cost(context):
    cart_page = CartPage(context.driver)
    total_price = cart_page.get_total_price()
    print(f"Total price from cart: '{total_price}'")  # Debugging line
    assert total_price.strip() == "$40.00"

def after_all(context):
    context.driver_setup.teardown_driver()