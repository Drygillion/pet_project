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

def test_open_inventory_item(authorized_page):
    inventory = InventoryPage(authorized_page)
    number = inventory.open_product_cart(Product.BACKPACK_NUMBER)
    check_url = InventoryItemPage(authorized_page)
    check_url.check_url(number)




