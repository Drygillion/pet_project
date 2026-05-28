# Playwright UI Automation Framework

Проект автоматизации UI-тестирования сайта SauceDemo, реализованный на Python с использованием:

* Python
* Playwright
* Pytest
* Page Object Model (POM)
* Allure Report
* Docker
* GitHub Actions CI/CD

---

# Описание проекта

Данный проект представляет собой полноценный automation framework для UI-тестирования веб-приложения.

В проекте реализованы:

* архитектура Page Object Model;
* переиспользуемые fixtures и assertions;
* Allure отчетность;
* Docker-контейнеризация;
* CI/CD через GitHub Actions;
* автоматическое создание скриншотов при падении тестов.

Framework покрывает полный пользовательский сценарий оформления заказа на сайте SauceDemo.

---

# Технологический стек

| Технология     | Назначение                     |
| -------------- | ------------------------------ |
| Python         | Основной язык программирования |
| Playwright     | UI автоматизация               |
| Pytest         | Тестовый framework             |
| POM            | Архитектура тестов             |
| Allure Report  | Отчетность                     |
| Docker         | Контейнеризация                |
| GitHub Actions | CI/CD                          |

---

# Структура проекта

```text
pet_project/
│
├── pages/
│   ├── base.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── inventory_item_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── logout.py
│   └── products.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_inventory_item.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_smoke.py
│
├── helpers/
│   └── screenshots/
│
├── allure-results/
├── allure-report/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── Dockerfile
├── docker-compose.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

# Реализованное тестовое покрытие

## Тесты авторизации

* успешный логин;
* проверка невалидного логина и пароля;
* проверка заблокированного пользователя;
* проверка текста ошибок.

## Тесты страницы товаров

* открытие карточки товара;
* добавление товара в корзину;
* удаление товара из корзины;
* проверка сортировки товаров;
* проверка цен товаров.

## Тесты корзины

* проверка открытия корзины;
* проверка сохранения товаров;
* удаление товаров;
* проверка корректности цен.

## Тесты оформления заказа

* проверка формы checkout;
* проверка итоговой суммы;
* проверка налога;
* проверка успешного оформления заказа.

## Smoke тест

Полный пользовательский сценарий:

1. Авторизация
2. Добавление товаров в корзину
3. Переход в корзину
4. Оформление заказа
5. Проверка итоговой суммы
6. Завершение заказа

---

# Возможности framework

* архитектура Page Object Model;
* переиспользуемые методы BasePage;
* динамические локаторы;
* переиспользуемые проверки;
* централизованные fixtures;
* автоматические скриншоты при падении тестов;
* запуск тестов в Docker;
* Allure отчетность;
* CI/CD интеграция через GitHub Actions.

---

# Docker

## Сборка и запуск контейнеров

```bash
docker-compose up --build
```

## Открытие Allure отчета

```text
http://localhost:5050/allure-docker-service/latest-report
```

---

# Allure Report

## Генерация Allure результатов

```bash
pytest --alluredir=allure-results
```

## Открытие локального Allure отчета

```bash
allure serve allure-results
```

---

# GitHub Actions CI/CD

Pipeline автоматически:

* устанавливает зависимости;
* устанавливает браузеры Playwright;
* запускает тесты;
* формирует Allure результаты;
* загружает artifacts.

---

# Установка проекта

## Клонирование репозитория

```bash
git clone https://github.com/Drygillion/pet_project.git
```

## Переход в папку проекта

```bash
cd pet_project
```

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

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Установка браузеров Playwright

```bash
playwright install
```

---

# Запуск тестов

## Запуск всех тестов

```bash
pytest
```

## Запуск smoke теста

```bash
pytest tests/test_smoke.py
```

## Запуск тестов с открытым браузером

```bash
pytest --headed
```

## Запуск конкретного теста

```bash
pytest tests/test_login.py
```

---

# Архитектура

Проект реализован с использованием паттерна Page Object Model (POM).

Каждая страница содержит:

* локаторы;
* методы работы со страницей;
* переиспользуемые проверки.

## Пример использования

```python
inventory = InventoryPage(page)

inventory.add_to_cart(Product.BACKPACK)

cart = inventory.open_cart()

assert cart.get_price(Product.BACKPACK_ID) == expected_price
```

---

# Скриншоты при падении тестов

При падении тестов framework автоматически сохраняет скриншоты в папку:

```text
helpers/screenshots/
```

---

# Автор

Automation QA Engineer

GitHub:
https://github.com/Drygillion
