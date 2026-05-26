from pages.products import Product
from pages.base import BasePage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect


class CartPage(BasePage):


    PRICE_BY_PRODUCT = '[data-test="inventory-item"]:has(a[id="item_{}_title_link"]) .inventory_item_price'
    CART_BADGE = ".shopping_cart_badge"
    CART = ".shopping_cart_link"
    """Кнопки"""
    CHECKOUT = "#checkout"
    CONTINUE_BUTTON = "#continue"

    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP_CODE = "#postal-code"
    ITEM_TOTAL='.summary_subtotal_label'
    TAX = '.summary_tax_label'
    TOTAL_SUM = '.summary_total_label'


    CART_URL = "https://www.saucedemo.com/cart.html"
    CART_ITEMS = ".cart_item"
    REMOVE_BUTTONS = '[data-test^="remove-"]'

    def open_cart(self):
        """Открыть корзину"""
        self.click(self.CART)


    def get_price(self, product_id):
        """Получить цену без знака доллара"""
        locator = Product.PRICE_BY_PRODUCT.format(product_id)
        price_text = self.page.locator(locator).inner_text()
        return float(price_text.replace("$", ""))

    def checkout(self):
        """Нажать на кнопку checkout. Переход на страницу checkout"""
        self.click(self.CHECKOUT)


    def fill_checkout_form(self, first_name: str, last_name: str, zip_code: str):
        """Заполняет форму оформления заказа"""
        self.fill(self.FIRST_NAME, f'{first_name}')
        self.fill(self.LAST_NAME, f'{last_name}')
        self.fill(self.ZIP_CODE, f'{zip_code}')
        self.click(self.CONTINUE_BUTTON)

    def get_summary_value(self, locator: str) -> float:
        """Возвращает числовое значение из элемента с ценой"""
        text = self.page.locator(locator).inner_text()
        # Извлекаем число после знака $
        if "$" in text:
            return float(text.split("$")[1])
        return float(text)

    def get_items_count(self) -> int:
        """Возвращает количество товаров в корзине"""
        return self.page.locator(self.CART_ITEMS).count()

    def remove_first_item(self):
        """Удаляет первый товар из корзины"""
        remove_btn = self.page.locator(self.REMOVE_BUTTONS).first
        if remove_btn.count():
            remove_btn.click()

    def remove_item_by_name(self, product_name: str):
        """Удаляет товар по имени из корзины"""
        locator = f'.cart_item:has-text("{product_name}") button'
        self.click(locator)

    def back_to_inventory(self):
        """Возвращается на страницу инвентаря"""
        self.page.go_back()

    def check_cart_is_empty(self):
        """Проверяет, что внутри корзины нет товаров"""
        expect(self.page.locator(self.CART_ITEMS)).to_have_count(0)

    def check_item_in_cart(self, product_name: str):
        """Проверяет, что конкретный товар есть в корзине"""
        locator = f'.cart_item:has-text("{product_name}")'
        expect(self.page.locator(locator)).to_be_visible()

    def proceed_to_checkout(self) -> CheckoutPage:
        """Нажимает Checkout и возвращает страницу оформления"""
        self.checkout()
        return CheckoutPage(self.page)

    def remove_item(self,product_name: str):
        """Удаляем товар из корзины"""
        locator = f'.cart_item:has-text("{product_name}") button'
        self.click(locator)

