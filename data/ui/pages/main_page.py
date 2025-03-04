from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page