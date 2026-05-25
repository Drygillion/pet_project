# Playwright UI Automation Framework

Проект автоматизации UI-тестирования для сайта SauceDemo, реализованный на Python с использованием Playwright, Pytest и архитектуры Page Object Model (POM).

---

# Технологический стек

* Python
* Playwright
* Pytest
* Page Object Model (POM)
* Allure Report
* GitHub

---

# Структура проекта

```text
pet_project/
│
├── pages/                     # Page Object классы
│   ├── base.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── inventory_item_page.py
│   ├── cart_page.py
│   ├── products.py
│   └── logout.py
│
├── tests/                     # UI тесты
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_smoke.py
│
├── helpers/
│   └── screenshots/           # Скриншоты при падении тестов
│
├── conftest.py                # Fixtures и hooks
├── requirements.txt
├── pytest.ini
└── README.md
```

---

#  Реализованный функционал

##  Тесты авторизации

* Проверка успешного логина
* Проверка невалидного логина
* Проверка текста ошибки

---

##  Тесты страницы товаров

* Открытие карточки товара
* Добавление товара в корзину
* Удаление товара из корзины
* Проверка сортировки товаров

---

## Тесты корзины

* Проверка добавленных товаров
* Проверка стоимости товаров
* Проверка количества товаров

---

## Тесты оформления заказа

* Проверка формы оформления
* Проверка итоговой суммы
* Проверка расчета налога и total price

---

## Smoke тест

Полный пользовательский сценарий:

* Авторизация
* Добавление товаров в корзину
* Переход в корзину
* Оформление заказа
* Проверка итоговой стоимости

---

# Возможности framework

* Архитектура Page Object Model
* Переиспользуемые методы BasePage
* Динамические локаторы
* Pytest fixtures
* Автоматическое создание скриншотов при падении тестов
* Переиспользуемые проверки (assertions)
* Проверка данных между страницами

---

# Установка проекта

## Клонирование репозитория

```bash
git clone https://github.com/Drygillion/pet_project.git
```

---

## Переход в папку проекта

```bash
cd pet_project
```

---

## Создание виртуального окружения

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Установка requirements.txt

```bash
pip install -r requirements.txt
```

---

# Установка Playwright

```bash
playwright install
```

---

# Запуск тестов

## Запуск всех тестов

```bash
pytest
```

---

## Запуск smoke теста

```bash
pytest tests/test_smoke.py
```

---

## Запуск тестов с открытием браузера

```bash
pytest --headed
```

---

# Allure Report

## Генерация Allure результатов

```bash
pytest --alluredir=allure-results
```

---

## Открытие Allure отчета

```bash
allure serve allure-results
```

---

# Архитектура тестов

Проект реализован с использованием паттерна Page Object Model (POM).

Каждая страница содержит:

* локаторы
* методы работы со страницей
* переиспользуемые проверки

---

## Пример использования

```python
inventory = InventoryPage(page)

inventory.add_to_cart(Product.BACKPACK)

cart = inventory.open_cart()

assert cart.get_price(Product.BACKPACK_ID) == expected_price
```

---

# Автор

Automation QA Engineer

GitHub:
https://github.com/Drygillion
