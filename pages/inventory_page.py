from pages.base import BasePage


class InventoryPage(BasePage):
    """Ссылки"""
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


    """Кнопка ADD"""
    ADD_TO_CART = '#add-to-cart-sauce-labs-{}'


    """Кнопка REMOVE"""
    REMOVE_FROM_CART = '#remove-sauce-labs-{}'

    """Кнопка корзины"""
    CART = '[data-test="shopping-cart-link"]'

    """Открыть карточку товара"""

    OPEN_PRODUCT = '#item_{}_title_link'

    def check_page_inventory_opened(self):
        self.check_url(self.INVENTORY_URL)

    def open_product_cart(self, product_number):
        locator = self.OPEN_PRODUCT.format(product_number)
        self.click(locator)

    def add_to_cart(self,product_name):
        locator = self.ADD_TO_CART.format(product_name)
        self.click(locator)

    def remove_from_cart(self,product_name):
        locator = self.REMOVE_FROM_CART.format(product_name)
        self.click(locator)

    def check_number_of_items_in_cart(self,number):
        self.check_text(self.CART, f'{number}')
