import pytest
from config.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.menu_page import MenuPage

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_logout(driver):
    login = LoginPage(driver)
    menu = MenuPage(driver)

    login.login("standard_user", "secret_sauce")
    menu.logout()


