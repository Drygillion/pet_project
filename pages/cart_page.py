
from pages.base import BasePage
from pages.products import Product


class CartPage(BasePage):


    PRICE_BY_PRODUCT = '[data-test="inventory-item"]:has(a[id="item_{}_title_link"]) .inventory_item_price'
    CART_BADGE = ".shopping_cart_badge"
    CART = ".shopping_cart_link"
    """Кнопки"""
    CHECKOUT = "#checkout"
    CONTINUE = "#continue"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP_CODE = "#postal-code"
    ITEM_TOTAL='.summary_subtotal_label'
    TAX = '.summary_tax_label'
    TOTAL_SUM = '.summary_total_label'

    def open_cart(self):
        self.click(self.CART)


    def get_price(self, product_id):
        locator = Product.PRICE_BY_PRODUCT.format(product_id)
        price_text = self.page.locator(locator).inner_text()
        return float(price_text.replace("$", ""))

    def checkout(self):
        self.click(self.CHECKOUT)

    def post_data(self,First_name,Last_name,Zip_code):
        self.fill(self.FIRST_NAME, f'{First_name}')
        self.fill(self.LAST_NAME, f'{Last_name}')
        self.fill(self.ZIP_CODE, f'{Zip_code}')
        self.click(self.CONTINUE)

    def get_summary_value_total(self, locator):

        price_text = self.page.locator(f'{locator}').inner_text()
        return float(price_text.split("$")[1])

    def get_summary_price(self, locator):
        price_text = self.page.locator(f'{locator}').inner_text()
        return float(price_text.replace("$", ""))