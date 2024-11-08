from driver_setup import DriverSetup

def before_all(context):
    """Runs once before all tests."""
    context.driver_setup = DriverSetup()
    context.driver = context.driver_setup.setup_driver()

def after_all(context):
    """Runs once after all tests."""
    context.driver_setup.teardown_driver(context.driver)


