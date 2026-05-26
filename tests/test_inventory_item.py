from pages.products import Product
from pages.cart_page import CartPage


def test_open_inventory_item(item_page_factory):
    """Открытие страницы товара"""
    item_page = item_page_factory(Product.BACKPACK_ID)
    # Проверяем, что открылся URL товара
    item_page.check_inventory_item_url(Product.BACKPACK_ID)


def test_check_inventory_item_cart(item_page_factory, inventory_page):
    """Добавление товара в корзину со страницы товара"""
    item_page = item_page_factory(Product.BIKE_LIGHT_ID)
    item_page.add_to_cart()
    # Проверяем, что бейдж на корзине имеет цифру 1
    inventory_page.check_number_of_items_in_cart('1')


def test_delete_inventory_item_from_cart(item_page_factory, inventory_page):
    """Удаление товара из корзины со страницы товара"""
    item_page = item_page_factory(Product.BIKE_LIGHT_ID)
    item_page.add_to_cart()
    inventory_page.check_number_of_items_in_cart('1')
    item_page.remove_from_cart()

    # Проверяем, что корзина пуста (бейдж отсутствует)
    inventory_page.check_cart_is_empty()