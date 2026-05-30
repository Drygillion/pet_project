from pages.products import Product
import allure

"""Информация о тесте"""
@allure.feature('Оформление заказа')
@allure.story("Smoke test")
@allure.title("Полный сценарий покупки товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_smoke(inventory_page):
    """Полный пользовательский сценарий"""

    with allure.step(f"Добавить товар '{Product.BACKPACK}' в корзину"):
        inventory_page.add_to_cart(Product.BACKPACK)
        price_backpack = inventory_page.get_price(Product.BACKPACK_ID)

    with allure.step(f"Добавить товар '{Product.BIKE_LIGHT}' в корзину"):
        inventory_page.add_to_cart(Product.BIKE_LIGHT)
        price_bike_light = inventory_page.get_price(Product.BIKE_LIGHT_ID)
        inventory_page.check_number_of_items_in_cart(2)


    with allure.step("Перейти в корзину"):
        cart = inventory_page.open_cart()

    with allure.step("Проверить соответствие цен в корзине"):
        assert price_backpack == cart.get_price(Product.BACKPACK_ID)
        assert price_bike_light == cart.get_price(Product.BIKE_LIGHT_ID)

    with allure.step("Заполнить форму оформления заказа"):
        cart.checkout()
        cart.fill_checkout_form("Maksim", "Testov", "123456")

    with allure.step("Проверить расчёт итоговой суммы"):
        item_total = cart.get_summary_value(cart.ITEM_TOTAL)
        tax = cart.get_summary_value(cart.TAX)
        calculated_total = item_total + tax
        actual_total = cart.get_summary_value(cart.TOTAL_SUM)

        assert calculated_total == actual_total, \
            f"Суммы не совпадают: ожидалось {calculated_total}, получено {actual_total}"