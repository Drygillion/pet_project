from pages.Inventory_item_page import InventoryItemPage
from pages.inventory_page import InventoryPage
from pages.products import Product
from tests.test_cart import CartPage


def test_open_inventory_item(authorized_page):
    inventory = InventoryPage(authorized_page)
    inventory.open_product_page(Product.BACKPACK_ID)
    check_url = InventoryItemPage(authorized_page)
    check_url.check_inventory_item_url(Product.BACKPACK_ID)


def test_check_inventory_item_cart(authorized_page):
    inventory = InventoryPage(authorized_page)
    inventory.open_product_page(Product.BIKE_LIGHT_ID)
    cart= InventoryItemPage(authorized_page)
    cart.add_to_cart()
    inventory.check_number_of_items_in_cart('1')

def test_delete_inventory_item_from_cart(authorized_page):
    inventory = InventoryPage(authorized_page)
    inventory.open_product_page(Product.BIKE_LIGHT_ID)
    cart= InventoryItemPage(authorized_page)
    cart.add_to_cart()
    inventory.check_number_of_items_in_cart('1')
    cart.remove_from_cart()
    cart = CartPage(authorized_page)
    cart.check_cart_is_empty()