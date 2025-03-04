
from playwright.sync_api import Page, expect

from data.ui.pages.main_page import MainPage


class MainPageCategory(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.__create_new_category = page.get_by_test_id("add-category-button")
        self.__new_category_textfield  = page.get_by_test_id("new-category-label")
        self.__category_textfield = page.get_by_test_id("category-edit")
        self.__category_list = page.locator('.category-list')
        self.__delete_category_button = page.get_by_test_id("category-option-delete-permanently")
        self.__rename_category_button = page.get_by_test_id("category-options-rename")

    def push_new_category_button(self):
        self.__create_new_category.click()

    def push_delete_category_button(self):
        self.__category_list.click(button="right")
        self.__delete_category_button.click()

    def push_rename_category_button(self):
        self.__category_list.click(button="right")
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
        expect(self.__category_list).to_contain_text(name_category)

    def validate_not_category_in_title(self, name_category: str):
        expect(self.__category_list).not_to_have_text(name_category)






