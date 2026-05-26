import pytest

from datetime import datetime

from config import BASE_URL
from pages.inventory_item_page import InventoryItemPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products import Product


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Функция создает скриншот при падении теста
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            timestamp = datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            page.screenshot(
                path=f"helpers/screenshots/{item.name}_{timestamp}.png"
            )

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 2560, "height": 1440},
        "ignore_https_errors": True,
        # Отключаем лишние ресурсы для ускорения
        "extra_http_headers": {
            "Accept-Language": "en-US,en;q=0.9",
        },
    }

def pytest_addoption(parser):
    """
    pytest опции
    """
    parser.addoption(
        "--username",
        action="store",
        default="standard_user"
    )

    parser.addoption(
        "--password",
        action="store",
        default="secret_sauce"
    )


@pytest.fixture()
def credentials(request):
    """
    Фикстура для входа
    """

    return {
        "username": request.config.getoption(
            "--username"
        ),
        "password": request.config.getoption(
            "--password"
        )
    }


@pytest.fixture()
def login_page(page):
    """
    Фикстура: Открытая страница логина.
    """
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    return login_page


@pytest.fixture()
def inventory_page(login_page, credentials, page):
    """
    Фикстура: Авторизованная страница инвентаря. После теста — автоматический выход.
    """
    inventory_page = login_page.login(
        username=credentials["username"],
        password=credentials["password"]
    )

    yield inventory_page

    # Очистка: выходим из системы
    from pages.logout import LogoutPage
    LogoutPage(page).logout()


@pytest.fixture()
def clean_inventory_page(inventory_page):
    """
    Фикстура: Инвентарь с очищенной корзиной.
    Удаляет все товары перед возвратом.
    """
    cart = inventory_page.open_cart()

    # Удаляем все товары из корзины
    while cart.get_items_count() > 0:
        cart.remove_first_item()

    # Возвращаемся в инвентарь
    cart.back_to_inventory()
    return inventory_page


@pytest.fixture()
def cart_page(inventory_page):
    """
    Фикстура: Страница корзины (простой переход).
    Использование: cart_page.checkout()
    """
    return inventory_page.open_cart()


@pytest.fixture()
def cart_with_items(inventory_page):
    """
    Фикстура: Корзина с двумя предустановленными товарами.
    """
    inventory_page.add_to_cart(Product.BACKPACK)
    inventory_page.add_to_cart(Product.BIKE_LIGHT)
    return inventory_page.open_cart()


@pytest.fixture()
def checkout_page(cart_with_items):
    """
    Фикстура: Страница оформления заказа.
    Корзина уже с товарами, нажат Checkout.
    """
    cart_with_items.checkout()
    return CheckoutPage(cart_with_items.page)


@pytest.fixture()
def item_page_factory(inventory_page):
    """
    Фикстура: Фабрика для создания страниц товаров.
    Использование: item_page = item_page_factory(Product.BACKPACK_ID)
    """

    def _create(product_id: str) -> InventoryItemPage:
        inventory_page.open_product_page(product_id)
        return InventoryItemPage(inventory_page.page)

    return _create


# ==================== ДОПОЛНИТЕЛЬНЫЕ ФИКСТУРЫ ДЛЯ НЕГАТИВНЫХ ТЕСТОВ ====================

@pytest.fixture()
def login_failed(page):
    """
    Фикстура: Неудачная попытка логина.
    Возвращает страницу логина с ошибкой.
    """
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login("invalid_user", "invalid_password")
    return login_page


@pytest.fixture()
def locked_user_login(page):
    """
    Фикстура: Логин заблокированного пользователя.
    """
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login("locked_out_user", "secret_sauce")
    return login_page