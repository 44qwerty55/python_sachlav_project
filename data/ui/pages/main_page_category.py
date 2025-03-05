from assertpy import assert_that
from playwright.sync_api import Page

from data.ui.pages.main_page import MainPage


class MainPageCategory(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.__create_new_category = page.get_by_test_id("add-category-button")
        self.__new_category_textfield = page.get_by_test_id("new-category-label")
        self.__category_textfield = page.get_by_test_id("category-edit")
        self.__category_list = page.locator('.category-list')
        self.__delete_category_button = page.get_by_test_id("category-option-delete-permanently")
        self.__rename_category_button = page.get_by_test_id("category-options-rename")
        self.__category_names_list = page.locator('.category-list .category-list-name')
        self.__category_menu = page.locator('div[data-testid="move-category"]')

    def push_new_category_button(self):
        self.__create_new_category.click()

    def clic_to_category_list(self):
        self.__category_list.click()

    def create_new_category(self, category_name: str):
        self.push_new_category_button()
        self.type_new_category(category_name)
        self.validate_name_category(category_name)

    def push_delete_category_button(self, category: str):
        self.click_menu_category_by_name(category)
        self.__delete_category_button.click()

    def push_rename_category_button(self, category: str):
        self.click_menu_category_by_name(category)
        self.__rename_category_button.click()

    def type_new_category(self, name: str):
        self.__new_category_textfield.fill(name)
        self.page.keyboard.press("Enter")

    def type_rename_category(self, name: str):
        self.__category_textfield.press("ControlOrMeta+a")
        self.__category_textfield.fill("")
        self.__category_textfield.fill(name)
        self.page.keyboard.press("Enter")

    def validate_name_category(self, name_category: str):
        assert_that(self.collect_all_category_name()).contains(name_category)

    def validate_not_category_in_title(self, name_category: str):
        # expect(self.__category_list).not_to_have_text(name_category)
        assert_that(self.collect_all_category_name()).does_not_contain(name_category)

    def collect_all_category_name(self) -> list:
        locator = self.__category_names_list
        count = locator.count()
        return [locator.nth(i).text_content().strip() for i in range(count)]

    def click_category_by_name(self, category_name: str):
        category_names = self.collect_all_category_name()
        locator = self.__category_names_list
        for i, name in enumerate(category_names):
            if name == category_name:
                locator.nth(i).click()
                return

    def click_menu_category_by_name(self, category_name: str):
        move_button_locator = self.__category_menu
        category_names = self.collect_all_category_name()
        for i, name in enumerate(category_names):
            if name == category_name:
                move_button_locator.nth(i).click()
                return
