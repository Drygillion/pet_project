
from pages.products import Product
from pages.cart_page import CartPage


def test_add_item_to_cart(inventory_page):
    """Добавление одного товара в корзину"""
    inventory_page.add_to_cart(Product.BACKPACK)
    inventory_page.check_number_of_items_in_cart(1)


def test_add_and_remove_items(inventory_page):
    """Добавление и удаление нескольких товаров"""
    inventory_page.add_to_cart(Product.BACKPACK)
    inventory_page.add_to_cart(Product.BIKE_LIGHT)
    inventory_page.check_number_of_items_in_cart(2)

    inventory_page.remove_from_cart(Product.BACKPACK)
    inventory_page.check_number_of_items_in_cart(1)

    inventory_page.remove_from_cart(Product.BIKE_LIGHT)

    # Проверяем, что корзина пуста
    cart = inventory_page.open_cart()
    cart.check_cart_is_empty()

def test_sort_price_low_to_high(inventory_page):
    """Сортировка от дешёвых к дорогим"""
    inventory_page.sort_products("lohi")
    actual_prices = inventory_page.get_all_prices()
    expected_prices = sorted(actual_prices)
    assert expected_prices == actual_prices

def test_sort_price_high_to_low(inventory_page):
    """Сортировка от дорогих к дешёвым"""
    inventory_page.sort_products("hilo")
    actual_prices = inventory_page.get_all_prices()
    expected_prices = sorted(actual_prices, reverse=True)
    assert expected_prices == actual_prices



