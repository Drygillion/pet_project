
from pages.inventory_page import InventoryPage
from pages.products import Product



def test_cart_price(authorized_page):
    inventory = InventoryPage(authorized_page)
    inventory.add_to_cart(Product.BACKPACK)
    price_backpack = inventory.get_price(Product.BACKPACK_ID)
    inventory.add_to_cart(Product.BIKE_LIGHT)
    price_bike_light = inventory.get_price(Product.BIKE_LIGHT_ID)
    inventory.check_number_of_items_in_cart('2')
    cart = inventory.open_cart()
    assert price_backpack == cart.get_price(Product.BACKPACK_ID)
    assert price_bike_light == cart.get_price(Product.BIKE_LIGHT_ID)

