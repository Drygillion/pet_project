from pages.base import BasePage


class CartPage(BasePage):
    '''Ссылка'''

    CART_BADGE = ".shopping_cart_badge"


    def check_cart_is_empty(self):
        self.check_element_hidden(self.CART_BADGE)