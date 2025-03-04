from assertpy import assert_that
from playwright.sync_api import Page, expect

from data.ui.pages.main_page import MainPage


class MainPageNote(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__create_new_note_button = page.get_by_test_id("sidebar-action-create-new-note")
        self.__preview_note_button = page.get_by_test_id("preview-mode")
        self.__delete_note_button = page.get_by_role("button", name="Delete note")
        self.__add_note_to_favorite_button = page.get_by_role("button", name="Add note to favorites")
        self.__write_in_note = page.get_by_role("textbox")
        self.__find_text_in_preview_mode = page.locator(".previewer.previewer_direction-ltr")
        self.__click_note_button = page.get_by_role("button", name="Notes", exact=True)
        self.__click_favorite_button = page.get_by_role("button", name="Favorites", exact=True)
        self.__click_trash_button = page.get_by_role("button", name="Trash", exact=True)
        self.__all_note_name_from_title = page.locator('div[data-testid^="note-title-"] div.truncate-text')


    def click_create_new_node_button(self):
        self.__create_new_note_button.click()

    def click_preview_mode_button(self):
        self.__preview_note_button.click()

    def click_delete_note_button(self):
        self.__delete_note_button.click()

    def click_add_note_to_favorite_button(self):
        self.__add_note_to_favorite_button.click()

    def write_in_node(self, text: str):
        self.__write_in_note.press_sequentially(text, delay=50)

    def write_name_and_value_in_node(self, name: str, value: str, enter: int):
        self.__write_in_note.press_sequentially(name, delay=50)
        for _ in range(enter):
            self.page.keyboard.press("Enter")
        self.__write_in_note.press_sequentially(value, delay=50)

    def create_new_node_node(self, name: str, value: str, enter: int):
        self.click_create_new_node_button()
        self.write_name_and_value_in_node(name, value, enter)

    def click_node_button(self):
        self.__click_note_button.click()

    def click_favorite_button(self):
        self.__click_favorite_button.click()

    def click_trash_button(self):
        self.__click_trash_button.click()

    def validate_node_in_preview(self, text: str):
        expect(self.__find_text_in_preview_mode).to_be_visible()
        expect(self.__find_text_in_preview_mode).to_contain_text(text, use_inner_text=True)

    def validate_node_in_title(self, name_node: str):
        assert_that(self.collect_all_note_texts()).contains(name_node)

    def validate_not_node_in_title(self, name_node: str):
        assert_that(self.collect_all_note_texts()).does_not_contain(name_node)

    def collect_all_note_texts(self) -> list:
        locator = self.__all_note_name_from_title
        count = locator.count()
        note_names = [locator.nth(i).text_content().strip() for i in range(count)]
        return note_names







