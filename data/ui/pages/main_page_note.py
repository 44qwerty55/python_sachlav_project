from assertpy import assert_that
from playwright.sync_api import Page, expect

from data.ui.constants.default_constance import DEFAULT_TEXT_IN_SCRATCHPAD
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
        self.__click_favorite_option_in_menu = page.get_by_test_id("note-option-favorite")
        self.__click_trash_button = page.get_by_role("button", name="Trash", exact=True)
        self.__click_trash_option_in_menu = page.get_by_test_id("note-option-trash")
        self.__move_to_category_option_in_menu = page.get_by_test_id("note-options-move-to-category-select")
        self.__all_note_name_from_title = page.locator('div[data-testid^="note-title-"] div.truncate-text')
        self.__click_sync_button = page.get_by_test_id("topbar-action-sync-notes")

        self.__click_scratchpad_button = page.get_by_role("button", name="Scratchpad", exact=True)
        self.__default_text_in_scratchpad = page.locator("pre").filter(has_text=DEFAULT_TEXT_IN_SCRATCHPAD)




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

    def click_favorite_option_in_menu(self):
        self.__click_favorite_option_in_menu.click()

    def click_trash_button(self):
        self.__click_trash_button.click()

    def click_trash_option_in_menu(self):
        self.__click_trash_option_in_menu.click()

    def click_sync_button(self):
        self.__click_sync_button.click()

    def select_category_move_to_category_option_in_menu(self, name: str):
        self.__move_to_category_option_in_menu.select_option(name)

    def click_scratchpad_button(self):
        self.__click_scratchpad_button.click()

    def write_value_in_node(self, value: str):
        self.__default_text_in_scratchpad.click()
        self.__write_in_note.press("ControlOrMeta+a")
        self.__write_in_note.fill("")
        self.__write_in_note.press_sequentially(value, delay=50)

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

    def click_note_by_name(self, note_name: str):
        locator = self.__all_note_name_from_title
        count = locator.count()

        for i in range(count):
            note_text = locator.nth(i).text_content().strip()
            if note_text == note_name:
                locator.nth(i).click(button="right")
                return







