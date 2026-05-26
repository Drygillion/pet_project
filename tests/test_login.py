


def test_valid_login(inventory_page):
    """Тест валидный логин и пароль, форма работает корректно"""
    inventory_page.check_page_inventory_opened()

def test_error_login(login_failed):
    """Сообщение об ошибке при неверном пароле"""
    login_failed.check_error_message("Epic sadface: Username and password do not match any user in this service")

