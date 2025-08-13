from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def add_first_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def sort_products(self, option_text):
        from selenium.webdriver.support.ui import Select
        select = Select(self.wait.until(lambda d: d.find_element(*self.SORT_DROPDOWN)))
        select.select_by_visible_text(option_text)


