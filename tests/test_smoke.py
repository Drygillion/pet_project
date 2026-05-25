from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.products import Product


def test_smoke(authorized_page):
    inventory = InventoryPage(authorized_page)
    inventory.add_to_cart(Product.BACKPACK)
    price_backpack = inventory.get_price(Product.BACKPACK_ID)
    inventory.add_to_cart(Product.BIKE_LIGHT)
    price_bike_light = inventory.get_price(Product.BIKE_LIGHT_ID)
    inventory.check_number_of_items_in_cart('2')
    cart = inventory.open_cart()
    assert price_backpack == cart.get_price(Product.BACKPACK_ID)
    assert price_bike_light == cart.get_price(Product.BIKE_LIGHT_ID)
    post = CartPage(authorized_page)
    post.checkout()
    post.post_data("Maksim","Testov", "123456")
    summary = price_backpack +  price_bike_light
    item_total = post.get_summary_value_total(CartPage.ITEM_TOTAL)
    assert summary == item_total
    tax = post.get_summary_value_total(CartPage.TAX)
    total_sum = float(tax + item_total)
    assert total_sum == post.get_summary_value_total(CartPage.TOTAL_SUM)

