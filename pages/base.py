from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def wait_for_element(self, locator):
        self.page.locator(locator).wait_for()

    def check_url(self, url):
        expect(self.page).to_have_url(url)

    def expect_element(self, locator):
        return expect(self.page.locator(locator))

    def check_text(self, locator, text):
        expect(self.page.locator(locator)).to_have_text(text)

    def check_element_hidden(self, locator):
        """Проверяет, что элемент отсутствует в DOM"""
        expect(self.page.locator(locator)).to_have_count(0)
