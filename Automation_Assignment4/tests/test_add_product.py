import pytest
from config.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_add_product(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login("standard_user", "secret_sauce")
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()
    cart.checkout()
    checkout.fill_info_and_continue("Akib", "Mahmud", "1234")
    checkout.finish_order()


