from pages.products import Product



def test_smoke(inventory_page):
    """Полный пользовательский сценарий"""
    # Добавляем товары и запоминаем цены
    inventory_page.add_to_cart(Product.BACKPACK)
    price_backpack = inventory_page.get_price(Product.BACKPACK_ID)

    inventory_page.add_to_cart(Product.BIKE_LIGHT)
    price_bike_light = inventory_page.get_price(Product.BIKE_LIGHT_ID)

    inventory_page.check_number_of_items_in_cart(2)

    # Переходим в корзину и проверяем цены
    cart = inventory_page.open_cart()
    assert price_backpack == cart.get_price(Product.BACKPACK_ID)
    assert price_bike_light == cart.get_price(Product.BIKE_LIGHT_ID)

    # Оформляем заказ
    cart.checkout()
    cart.fill_checkout_form("Maksim", "Testov", "123456")


    # Проверяем итоговую сумму
    item_total = cart.get_summary_value(cart.ITEM_TOTAL)
    tax = cart.get_summary_value(cart.TAX)
    calculated_total = item_total + tax
    actual_total = cart.get_summary_value(cart.TOTAL_SUM)

    assert calculated_total == actual_total