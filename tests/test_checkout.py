from pages.checkout_page import CheckoutPage
from pages.products import Product


def test_checkout_total_calculation(inventory_page):
    """Проверка расчёта итоговой суммы при оформлении"""
    # Добавляем два товара
    inventory_page.add_to_cart(Product.BACKPACK)
    inventory_page.add_to_cart(Product.BIKE_LIGHT)

    # Переходим в корзину и оформляем
    cart = inventory_page.open_cart()
    cart.checkout()
    cart.fill_checkout_form("Maksim", "Testov", "123456")

    # Проверяем суммы
    item_total = cart.get_summary_value(cart.ITEM_TOTAL)
    tax = cart.get_summary_value(cart.TAX)
    calculated_total = item_total + tax
    actual_total = cart.get_summary_value(cart.TOTAL_SUM)

    assert calculated_total == actual_total


def test_complete_checkout(inventory_page):
    """Полное оформление заказа до конца"""
    inventory_page.add_to_cart(Product.BACKPACK)

    cart = inventory_page.open_cart()
    cart.checkout()
    cart.fill_checkout_form("Maksim", "Testov", "123456")

    checkout = CheckoutPage(cart.page)
    checkout.finish_checkout()
    # Проверяем успешное завершение
    checkout.check_success_message("Thank you for your order!")