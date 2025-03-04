import pytest
from playwright.sync_api import Page

from data.ui.constants.default_constance import NEW_NOTE_NAME, NEW_NOTE_VALUE
from data.ui.constants.urls_data import MAIN_PAGE_URL
from data.ui.pages.main_page import MainPage
from data.ui.pages.main_page_category import MainPageCategory
from data.ui.pages.main_page_note import MainPageNote


@pytest.fixture
def main_page(page: Page):
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto(MAIN_PAGE_URL)
    return MainPage(page)

@pytest.fixture
def category_page(main_page):
    return MainPageCategory(main_page.page)

@pytest.fixture
def note_page(main_page):
    return MainPageNote(main_page.page)

@pytest.fixture
def generate_new_note_name():
    return NEW_NOTE_NAME

@pytest.fixture
def generate_new_note_value():
    return NEW_NOTE_VALUE
