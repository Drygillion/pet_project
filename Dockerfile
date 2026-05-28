FROM mcr.microsoft.com/playwright/python:v1.48.0-jammy

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["pytest", "-v", "--browser=chromium", "--alluredir=allure-results"]