from pages.checkout_page import CheckoutPage
from pages.products import Product
import allure

@allure.feature("Оформление заказа")
@allure.story("Расчёт суммы")
@allure.title("Проверка расчёта итоговой суммы при оформлении")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_total_calculation(inventory_page):
    """Проверка расчёта итоговой суммы при оформлении"""

    with allure.step(f"Добавить товар '{Product.BACKPACK}' в корзину"):
       inventory_page.add_to_cart(Product.BACKPACK)

    with allure.step(f"Добавить товар '{Product.BIKE_LIGHT}' в корзину"):
        inventory_page.add_to_cart(Product.BIKE_LIGHT)

    with allure.step("Перейти в корзину"):
        cart = inventory_page.open_cart()

    with allure.step("Перейти к информации о клиенте"):
         cart.checkout()

    with allure.step("Заполнить форму информацией о клиенте"):
        cart.fill_checkout_form("Maksim", "Testov", "123456")

    with allure.step("Получить суммы на странице подтверждения"):
        checkout = CheckoutPage(cart.page)
        item_total = checkout.get_item_total()
        tax = checkout.get_tax()
        actual_total = checkout.get_total()

        allure.attach(str(item_total), "Сумма товаров", allure.attachment_type.TEXT)
        allure.attach(str(tax), "Налог", allure.attachment_type.TEXT)
        allure.attach(str(actual_total), "Итоговая сумма", allure.attachment_type.TEXT)

    with allure.step("Проверить, что сумма товаров + налог = итоговая сумма"):
        calculated_total = item_total + tax
        assert calculated_total == actual_total, \
            f"Суммы не совпадают. Ожидалось: {calculated_total}, Получено: {actual_total}"


@allure.feature("Оформление заказа")
@allure.story("Полный сценарий")
@allure.title("Полное оформление заказа до конца")
@allure.severity(allure.severity_level.CRITICAL)
def test_complete_checkout(inventory_page):
    """Полное оформление заказа до конца с получением сообщения об успешном завершении"""
    with allure.step(f"Добавить товар '{Product.BACKPACK}' в корзину"):
        inventory_page.add_to_cart(Product.BACKPACK)

    with allure.step("Перейти в корзину"):
        cart = inventory_page.open_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart.checkout()

    with allure.step("Заполнить форму информацией о клиенте"):
        cart.fill_checkout_form("Maksim", "Testov", "123456")

    with allure.step("Завершить оформление заказа (Finish)"):
        checkout = CheckoutPage(cart.page)
        checkout.finish_checkout()

    with allure.step("Проверить сообщение об успешном заказе"):
        checkout.check_success_message("Thank you for your order!")