from pages.Inventory_item_page import InventoryItemPage
from pages.base import BasePage
from pages.inventory_page import InventoryPage
from pages.products import Product
from tests.test_cart import CartPage


def test_add_item_to_cart(authorized_page):
    inventory = InventoryPage(authorized_page)
    inventory.add_to_cart(Product.BACKPACK)
    inventory.check_number_of_items_in_cart('1')

def test_add_item_to_cart_and_remove(authorized_page):
    inventory = InventoryPage(authorized_page)
    inventory.add_to_cart(Product.BACKPACK)
    inventory.add_to_cart(Product.BIKE_LIGHT)
    inventory.check_number_of_items_in_cart('2')
    inventory.remove_from_cart(Product.BACKPACK)
    inventory.check_number_of_items_in_cart('1')
    inventory.remove_from_cart(Product.BIKE_LIGHT)
    cart = CartPage(authorized_page)
    cart.check_cart_is_empty()

def test_sort_price_low_to_high(authorized_page):
    inventory = InventoryPage(authorized_page)
    inventory.sort_products("lohi")
    actual_prices = inventory.get_all_prices()
    exepected_prices = sorted(actual_prices)
    assert exepected_prices == actual_prices

def test_sort_price_high_to_low(authorized_page):
    inventory = InventoryPage(authorized_page)
    inventory.sort_products("hilo")
    actual_prices = inventory.get_all_prices()
    exepected_prices = sorted(actual_prices, reverse=True)
    assert exepected_prices == actual_prices



