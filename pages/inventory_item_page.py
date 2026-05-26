from pages.base import BasePage


class InventoryItemPage(BasePage):
    CARTPAGE_URL = "https://www.saucedemo.com/inventory-item.html?id={}"
    ADD_TO_CART = '#add-to-cart'
    REMOVE_FROM_CART = '#remove'


    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def remove_from_cart(self):
        self.click(self.REMOVE_FROM_CART)

    def check_inventory_item_url(self, number):
        expected_url = self.CARTPAGE_URL.format(number)
        self.check_url(expected_url)
