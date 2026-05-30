import allure
from pages.products import Product


@allure.feature("Каталог товаров")
@allure.story("Добавление в корзину")
@allure.title("Добавление одного товара в корзину")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_cart(inventory_page):
    """Добавление одного товара в корзину"""
    with allure.step(f"Добавить товар '{Product.BACKPACK}' в корзину"):
        inventory_page.add_to_cart(Product.BACKPACK)
    with allure.step("Проверить счетчик корзины"):
        inventory_page.check_number_of_items_in_cart(1)

@allure.feature("Каталог товаров")
@allure.story("Удаление из корзины")
@allure.title("Добавление и удаление нескольких товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_and_remove_items(inventory_page):
    """Добавление и удаление нескольких товаров"""
    with allure.step(f"Добавить товар '{Product.BACKPACK}' в корзину"):
        inventory_page.add_to_cart(Product.BACKPACK)

    with allure.step(f"Добавить товар '{Product.BIKE_LIGHT}' в корзину"):
        inventory_page.add_to_cart(Product.BIKE_LIGHT)

    with allure.step("Проверить счетчик корзины (ожидается 2)"):
        inventory_page.check_number_of_items_in_cart(2)
    with allure.step(f"Удалить товар '{Product.BACKPACK}' из корзины"):
        inventory_page.remove_from_cart(Product.BACKPACK)
    with allure.step("Проверить счетчик корзины (ожидается 1)"):
        inventory_page.check_number_of_items_in_cart(1)

    with allure.step(f"Удалить товар '{Product.BIKE_LIGHT}' из корзины"):
        inventory_page.remove_from_cart(Product.BIKE_LIGHT)

    with allure.step("Проверить, что корзина пуста"):
        cart = inventory_page.open_cart()
        cart.check_cart_is_empty()



@allure.feature("Каталог товаров")
@allure.story("Сортировка")
@allure.title("Сортировка товаров от дешёвых к дорогим")
@allure.severity(allure.severity_level.NORMAL)
def test_sort_price_low_to_high(inventory_page):
    """Сортировка от дешёвых к дорогим"""
    with allure.step("Выбрать сортировку 'Price (low to high)'"):
        inventory_page.sort_products("lohi")

    with allure.step("Получить цены всех товаров"):
        actual_prices = inventory_page.get_all_prices()
        expected_prices = sorted(actual_prices)

    with allure.step("Проверить, что цены отсортированы правильно"):
        assert expected_prices == actual_prices

@allure.feature("Каталог товаров")
@allure.story("Сортировка")
@allure.title("Сортировка товаров от дорогих к дешёвым")
@allure.severity(allure.severity_level.NORMAL)
def test_sort_price_high_to_low(inventory_page):
    """Сортировка от дорогих к дешёвым"""
    with allure.step("Выбрать сортировку 'Price (high to low)'"):
        inventory_page.sort_products("hilo")

    with allure.step("Получить цены всех товаров"):
        actual_prices = inventory_page.get_all_prices()
        expected_prices = sorted(actual_prices, reverse=True)

    with allure.step("Проверить, что цены отсортированы правильно"):
        assert expected_prices == actual_prices



