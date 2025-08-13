from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CANCEL_BTN = (By.ID, "cancel")

    def fill_info_and_continue(self, fname, lname, postal):
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BTN)

    def finish_order(self):
        self.click(self.FINISH_BTN)

    def cancel_checkout(self):
        self.click(self.CANCEL_BTN)


