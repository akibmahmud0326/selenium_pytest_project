from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    REMOVE_BTN = (By.XPATH, "//button[contains(text(),'Remove')]")

    def checkout(self):
        self.click(self.CHECKOUT_BTN)

    def remove_item(self):
        self.click(self.REMOVE_BTN)


