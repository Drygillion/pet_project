from pages.cart_page import CartPage
from pages.products import Product


def test_cart_page_opened(inventory_page):
    """Переход в корзину со страницы инвентаря"""
    cart = inventory_page.open_cart()
    cart.check_url(CartPage.CART_URL)


def test_item_price_in_cart(inventory_page):
    """Цена товара в корзине соответствует цене в каталоге"""
    # Добавляем товар
    inventory_page.add_to_cart(Product.BACKPACK)
    price_in_inventory = inventory_page.get_price(Product.BACKPACK_ID)

    # Переходим в корзину
    cart = inventory_page.open_cart()
    price_in_cart = cart.get_price(Product.BACKPACK_ID)

    assert price_in_inventory == price_in_cart


def test_remove_item_from_cart(inventory_page):
    """Удаление товара из корзины"""
    # Добавляем товар
    inventory_page.add_to_cart(Product.BACKPACK)
    inventory_page.check_number_of_items_in_cart(1)

    # Переходим в корзину
    cart = inventory_page.open_cart()
    cart.remove_item(Product.BACKPACK)

    # Возвращаемся в инвентарь
    inventory_page.page.go_back()
    inventory_page.check_cart_is_empty()

def test_cart_price(inventory_page):
    inventory_page.add_to_cart(Product.BACKPACK)
    price_backpack = inventory_page.get_price(Product.BACKPACK_ID)
    inventory_page.add_to_cart(Product.BIKE_LIGHT)
    price_bike_light = inventory_page.get_price(Product.BIKE_LIGHT_ID)
    inventory_page.check_number_of_items_in_cart('2')
    cart = inventory_page.open_cart()
    assert price_backpack == cart.get_price(Product.BACKPACK_ID)
    assert price_bike_light == cart.get_price(Product.BIKE_LIGHT_ID)

