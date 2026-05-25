from pages.base import BasePage
from pages.products import Product
from pages.cart_page import CartPage

class InventoryPage(BasePage):
    """Ссылки"""
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


    """Кнопка ADD"""
    ADD_TO_CART = '#add-to-cart-sauce-labs-{}'


    """Кнопка REMOVE"""
    REMOVE_FROM_CART = '#remove-sauce-labs-{}'

    """Кнопка корзины"""
    CART = '.shopping_cart_link'

    """Количество предметов в корзине"""
    CART_BADGE = ".shopping_cart_badge"

    """Открыть карточку товара"""
    OPEN_PRODUCT = '#item_{}_title_link'

    """Локатор всех цен"""
    ITEM_PRICES = ".inventory_item_price"

    """Сортировка на странице продуктов"""
    PRODUCT_SORT = '[data-test="product-sort-container"]'



    def check_page_inventory_opened(self):
        self.check_url(self.INVENTORY_URL)

    def open_product_page(self, product_number):
        locator = self.OPEN_PRODUCT.format(product_number)
        self.click(locator)

    def add_to_cart(self,product_name):
        locator = self.ADD_TO_CART.format(product_name)
        self.click(locator)

    def remove_from_cart(self,product_name):
        locator = self.REMOVE_FROM_CART.format(product_name)
        self.click(locator)

    def check_number_of_items_in_cart(self,number):
        self.check_text(self.CART_BADGE, f'{number}')

    def get_all_prices(self):
        prices  = self.page.locator(self.ITEM_PRICES).all_inner_texts()
        return [float(price.replace('$', ' ')) for price in prices]

    """Метод выбора сортировки"""
    def sort_products(self, value):
        self.page.locator(self.PRODUCT_SORT).select_option(value) # az -От A до Z сортировка, ZA - от Z до A, lohi - цена от Low к High, hilo - цена от High к Low

    def get_price(self, product_id):
        locator = Product.PRICE_BY_PRODUCT.format(product_id)
        price_text = self.page.locator(locator).inner_text()
        return float(price_text.replace("$", ""))

    def open_cart(self):
        self.click(self.CART)
        return CartPage(self.page)