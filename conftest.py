import pytest

from datetime import datetime

from config import BASE_URL

from pages.base import BasePage
from pages.login_page import LoginPage
from pages.logout import LogoutPage


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Функция создает скриншот при падении теста"""
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
def browser_context_args():
    """Playwright размеры окна выполнения теста"""
    return {
        "viewport": {
            "width": 2560,
            "height": 1440
        }
    }

def pytest_addoption(parser):
    """pytest опции"""
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
    """фикстура для входа"""

    return {
        "username": request.config.getoption(
            "--username"
        ),
        "password": request.config.getoption(
            "--password"
        )
    }


@pytest.fixture()
def authorized_page(page, credentials):
    """
    Авторизация пользователя
    """

    login_page = LoginPage(page)

    login_page.open(BASE_URL)

    login_page.login(
        username=credentials["username"],
        password=credentials["password"]
    )

    yield page

    LogoutPage(page).logout()



@pytest.fixture()
def invalid_login(page):
    """Логин невалидным пользователем"""

    login_page = LoginPage(page)

    login_page.open(BASE_URL)

    login_page.login(
        username="invalid_user",
        password="invalid_password"
    )

    return login_page



