from playwright.sync_api import expect

from pages.inventory_page import InventoryPage



def test_success_login(authorized_page):
    """Тест валидный логин и пароль, форма работает корректно"""
    login = InventoryPage(authorized_page)
    login.check_page_inventory_opened()

def test_error_login(invalid_login):
    """Сообщение об ошибке при неверном пароле"""

    invalid_login.check_error_message("Epic sadface: Username and password do not match any user in this service")

