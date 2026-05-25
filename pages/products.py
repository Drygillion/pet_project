from pages.base import BasePage


class Product(BasePage):
    """product_name Продукты(одежда)"""
    BACKPACK = "backpack"
    BIKE_LIGHT = "bike-light"
    BOLT_T_SHIRT = "bolt-t-shirt"
    FLEECE_JACKET = "fleece-jacket"

    """product_ID"""
    BACKPACK_ID= "4"
    BIKE_LIGHT_ID = "0"
    T_SHIRT_ID = "1"
    JACKET_ID = "5"

    """Цена по id продукта"""
    PRICE_BY_PRODUCT = '[data-test="inventory-item"]:has(a[id="item_{}_title_link"]) .inventory_item_price'