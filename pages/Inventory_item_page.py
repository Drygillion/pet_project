from pages.base import BasePage


class InventoryItemPage(BasePage):
    CARTPAGE_URL = "https://www.saucedemo.com/inventory-item.html?id={}"
    ADD_TO_CART = '#add-to-cart'

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def check_url(self, number):
        self.click(self.CARTPAGE_URL.format(number))
