import allure

@allure.feature("Авторизация")
@allure.story("Успешный вход")
@allure.title("Вход с валидными учетными данными")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(inventory_page):
    """Тест валидный логин и пароль, форма работает корректно, открывается страница товара"""
    with allure.step("Проверить, что открыта страница товара"):
        inventory_page.check_page_inventory_opened()


@allure.feature("Авторизация")
@allure.story("Неудачный вход")
@allure.title("Вход с невалидными учетными данными")
@allure.severity(allure.severity_level.NORMAL)
def test_error_login(login_failed):
    """Сообщение об ошибке при неверном пароле"""
    with allure.step("Проверить сообщение об ошибке"):
        login_failed.check_error_message("Epic sadface:  WRONG ERROR MESSAGE")  #"Тест упал намеренно для проверки скриншотов"

@allure.feature("Авторизация")
@allure.story("Заблокированный пользователь")
@allure.title("Вход заблокированного пользователя")
@allure.severity(allure.severity_level.NORMAL)
def test_locked_user_login(locked_user_login):
    """Заблокированный пользователь не может войти"""
    with allure.step("Проверить сообщение об ошибке для locked_out_user"):
        locked_user_login.check_error_message(
            "Epic sadface: Sorry, this user has been locked out."
        )