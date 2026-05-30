from pages.base import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    USERNAME_INPUT = "[id='user-name']"
    PASSWORD_INPUT = "[id='password']"
    LOGIN_BUTTON = "[id='login-button']"
    URL = "https://www.saucedemo.com"
    ERROR_MESSAGE_LOGIN = "[data-test='error']"

    def open(self,url):
        self.page.goto(url, timeout=120000)
        self.page.locator('#user-name').wait_for(state="visible", timeout=30000)



    def login(self,username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return InventoryPage(self.page)

    def check_error_message(self, text):
        self.check_text(self.ERROR_MESSAGE_LOGIN, text)