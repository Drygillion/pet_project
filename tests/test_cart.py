from pages.cart_page import CartPage
from pages.products import Product
import allure

@allure.feature("Корзина")
@allure.story("Навигация")
@allure.title("Переход на страницу корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_cart_page_opened(inventory_page):
    """Переход в корзину со страницы инвентаря"""
    with allure.step("Перейти в корзину"):
        cart = inventory_page.open_cart()

    with allure.step("Проверить URL страницы корзины"):
        cart.check_url(CartPage.CART_URL)


@allure.feature("Корзина")
@allure.story("Цены")
@allure.title("Цена товара в корзине соответствует цене в каталоге")
@allure.severity(allure.severity_level.CRITICAL)
def test_item_price_in_cart(inventory_page):
    """Цена товара в корзине соответствует цене в каталоге"""
    with allure.step(f"Добавить товар '{Product.BACKPACK}' в корзину"):
        inventory_page.add_to_cart(Product.BACKPACK)
        price_in_inventory = inventory_page.get_price(Product.BACKPACK_ID)
        allure.attach(str(price_in_inventory), "Цена в каталоге", allure.attachment_type.TEXT)



    with allure.step("Перейти в корзину"):
        cart = inventory_page.open_cart()
    with allure.step("Получить цену товара в корзине"):
        price_in_cart = cart.get_price(Product.BACKPACK_ID)
        allure.attach(str(price_in_cart), "Цена в корзине", allure.attachment_type.TEXT)

    with allure.step("Проверить, что цены совпадают"):
        assert price_in_inventory == price_in_cart, f"Цены не совпадают: {price_in_inventory} vs {price_in_cart}"


@allure.feature("Корзина")
@allure.story("Удаление")
@allure.title("Удаление товара из корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_remove_item_from_cart(inventory_page):
    """Удаление товара из корзины"""

    with allure.step(f"Добавить товар '{Product.BACKPACK}' в корзину"):
        inventory_page.add_to_cart(Product.BACKPACK)

    with allure.step("Проверить счетчик корзины (ожидается 1)"):
        inventory_page.check_number_of_items_in_cart(1)

    with allure.step("Перейти в корзину"):
        cart = inventory_page.open_cart()

    with allure.step(f"Удалить товар '{Product.BACKPACK}' из корзины"):
        cart.remove_item(Product.BACKPACK)

    with allure.step("Вернуться в каталог и проверить, что корзина пуста"):
        inventory_page.page.go_back()
        inventory_page.check_cart_is_empty()

@allure.feature("Корзина")
@allure.story("Цены")
@allure.title("Проверка цен в корзине")
@allure.severity(allure.severity_level.CRITICAL)
def test_cart_price(inventory_page):
    with allure.step(f"Добавить товар '{Product.BACKPACK}' в корзину"):
        inventory_page.add_to_cart(Product.BACKPAC)

    with allure.step(f"Получить цену товара '{Product.BIKE_LIGHT}' в каталоге"):
        price_backpack = inventory_page.get_price(Product.BACKPACK_ID)
        allure.attach(str(price_backpack), "Цена в каталоге", allure.attachment_type.TEXT)

    with allure.step(f"Добавить товар '{Product.BIKE_LIGHT}' в корзину"):
        inventory_page.add_to_cart(Product.BIKE_LIGHT)

    with allure.step(f"Получить цену товара '{Product.BIKE_LIGHT}' в каталоге"):
        price_bike_light = inventory_page.get_price(Product.BIKE_LIGHT_ID)
        allure.attach(str(price_backpack), "Цена в каталоге", allure.attachment_type.TEXT)

    with allure.step("Проверить счетчик корзины (ожидается 1)"):
        inventory_page.check_number_of_items_in_cart('2')

    with allure.step("Перейти в корзину"):
        cart = inventory_page.open_cart()

    with allure.step("Проверить, что цены в корзине и каталоге совпадают"):
        assert price_backpack == cart.get_price(Product.BACKPACK_ID)
        assert price_bike_light == cart.get_price(Product.BIKE_LIGHT_ID)

