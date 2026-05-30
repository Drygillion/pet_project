from pages.products import Product
import allure


@allure.feature("Страница товара")
@allure.story("Открытие страницы")
@allure.title("Открытие страницы конкретного товара")
@allure.severity(allure.severity_level.NORMAL)
def test_open_inventory_item(item_page_factory):
    """Открытие страницы товара"""
    with allure.step(f"Открыть страницу товара '{Product.BACKPACK}'"):
        item_page = item_page_factory(Product.BACKPACK_ID)

    with allure.step("Проверить URL страницы товара"):
        item_page.check_inventory_item_url(Product.BACKPACK_ID)

@allure.feature("Страница товара")
@allure.story("Добавление в корзину")
@allure.title("Добавление товара в корзину со страницы товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_check_inventory_item_cart(item_page_factory, inventory_page):
    """Добавление товара в корзину со страницы товара"""
    with allure.step(f"Открыть страницу товара '{Product.BIKE_LIGHT}'"):
        item_page = item_page_factory(Product.BIKE_LIGHT_ID)

    with allure.step("Добавить товар в корзину"):
        item_page.add_to_cart()

    with allure.step("Проверить счетчик корзины"):
        inventory_page.check_number_of_items_in_cart('1')

@allure.feature("Страница товара")
@allure.story("Удаление из корзины")
@allure.title("Удаление товара из корзины со страницы товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_inventory_item_from_cart(item_page_factory, inventory_page):
    """Удаление товара из корзины со страницы товара"""
    with allure.step(f"Открыть страницу товара '{Product.BIKE_LIGHT}'"):
        item_page = item_page_factory(Product.BIKE_LIGHT_ID)

    with allure.step("Добавить товар в корзину"):
        item_page.add_to_cart()

    with allure.step("Проверить счетчик корзины (ожидается 1)"):
        inventory_page.check_number_of_items_in_cart('1')

    with allure.step("Удалить товар из корзины"):
        item_page.remove_from_cart()

    with allure.step("Проверить, что корзина пуста,бэйдж счетчика отсуствует "):
        inventory_page.check_cart_is_empty()