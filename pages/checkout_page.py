from pages.base import BasePage
from playwright.sync_api import expect


class CheckoutPage(BasePage):
    """Страница оформления заказа (Checkout)"""
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    CANCEL_BUTTON = "#cancel"

    """Страница Overview """
    ITEM_TOTAL = ".summary_subtotal_label"
    TAX = ".summary_tax_label"
    TOTAL = ".summary_total_label"
    FINISH_BUTTON = "#finish"
    """Страница Complete"""
    SUCCESS_MESSAGE = ".complete-header"
    BACK_HOME_BUTTON = "#back-to-products"
    PONY_EXPRESS_IMAGE = ".pony_express"


    def fill_customer_info(self, first_name: str, last_name: str, zip_code: str):
        """Заполняет форму информации о клиенте"""
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.ZIP_CODE, zip_code)

    def continue_checkout(self):
        """Нажимает Continue и переходит к Overview"""
        self.click(self.CONTINUE_BUTTON)

    def cancel_checkout(self):
        """Отменяет оформление заказа"""
        self.click(self.CANCEL_BUTTON)

    def get_item_total(self) -> float:
        """Возвращает сумму товаров (Item total)"""
        text = self.page.locator(self.ITEM_TOTAL).inner_text()
        return float(text.replace("Item total: $", ""))

    def get_tax(self) -> float:
        """Возвращает сумму налога (Tax)"""
        text = self.page.locator(self.TAX).inner_text()
        return float(text.replace("Tax: $", ""))

    def get_total(self) -> float:
        """Возвращает итоговую сумму (Total)"""
        text = self.page.locator(self.TOTAL).inner_text()
        return float(text.replace("Total: $", ""))

    def finish_checkout(self):
        """Нажимает Finish и завершает заказ"""
        self.click(self.FINISH_BUTTON)


    def check_success_message(self, expected_text: str = "Thank you for your order!"):
        """Проверяет сообщение об успешном заказе"""
        self.check_text(self.SUCCESS_MESSAGE, expected_text)

    def check_pony_express_visible(self):
        """Проверяет, что видно изображение Pony Express"""
        expect(self.page.locator(self.PONY_EXPRESS_IMAGE)).to_be_visible()

    def back_home(self):
        """Возвращается на главную страницу (инвентарь)"""
        self.click(self.BACK_HOME_BUTTON)

