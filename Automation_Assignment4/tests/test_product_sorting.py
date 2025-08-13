import pytest
from config.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPa

ge

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_product_sorting(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")
    inventory.sort_products("Price (low to high)")
