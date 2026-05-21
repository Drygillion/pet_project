from playwright.sync_api import Page
from pages.base import BasePage

class LogoutPage(BasePage):
    MENU = '[id="react-burger-menu-btn"]'
    LOGOUT ='[id="logout_sidebar_link"]'

    def logout(self):

        self.click(self.MENU)
        self.click(self.LOGOUT)
        assert self.page.url == "https://www.saucedemo.com/"