from playwright.sync_api import expect

from pages.base import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "[id='user-name']"
    PASSWORD_INPUT = "[id='password']"
    LOGIN_BUTTON = "[id='login-button']"
    URL = "https://www.saucedemo.com"
    ERROR_MESSAGE_LOGIN = "[data-test='error']"

    def open(self,url):
        self.page.goto(url,wait_until="domcontentloaded",timeout=60000)



    def login(self,username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def check_error_message(self, text):
        self.check_text(self.ERROR_MESSAGE_LOGIN, text)