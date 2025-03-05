import json

from playwright.async_api import Page

from data.ui.pages.main_page import MainPage

class LocalStorage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def get_local_storage(self):
        return self.page.evaluate("JSON.stringify(localStorage);")

