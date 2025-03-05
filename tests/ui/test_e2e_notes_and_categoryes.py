import allure
import pytest
from assertpy import assert_that

from data.ui.helpers import helper
from data.ui.helpers.local_storage_helper import LocalStorageHelper
from data.ui.pages.local_storage import LocalStorage

count_push_enter = 3

@pytest.mark.positive
@pytest.mark.ui
@pytest.mark.e2e
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("UI E2E move note to category test")
def test_move_to_category_menu(note_page, category_page, new_note_name, new_note_value, new_category_name):
    category_page.create_new_category(new_category_name)
    note_page.create_new_node_node(new_note_name, new_note_value, count_push_enter)
    note_page.click_note_by_name(new_note_name)
    note_page.select_category_move_to_category_option_in_menu(new_category_name)
    category_page.clic_to_category_list()
    note_page.validate_node_in_title(new_note_name)

    with allure.step("Assert note in LocalStorage"):
        note_page.click_sync_button()
        local_storage = LocalStorage(note_page.page)
        storage_data = local_storage.get_local_storage()
        note_in_local_storage = LocalStorageHelper.get_note_by_name(storage_data, new_note_name)
        expected_text = helper.create_formatted_string(new_note_name, new_note_value, count_push_enter)
        assert_that(note_in_local_storage.get_text()).is_equal_to(expected_text)
        assert_that(note_in_local_storage.get_category().get_name()).is_equal_to(new_category_name)

@pytest.mark.positive
@pytest.mark.ui
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("UI create note and when delete from trash test")
def test_delete_from_menu(note_page, new_note_name, new_note_value):
    note_page.add_new_note_to_trash(new_note_name, new_note_value, count_push_enter)
    note_page.click_trash_button()
    note_page.validate_node_in_title(new_note_name)
    note_page.click_note_by_name(new_note_name)
    note_page.delete_note_from_trash()
    note_page.validate_not_node_in_title(new_note_name)

    with allure.step("Assert note in LocalStorage"):
        note_page.click_sync_button()
        local_storage = LocalStorage(note_page.page)
        storage_data = local_storage.get_local_storage()
        list_notes_in_local_storage = LocalStorageHelper.parse_notes(storage_data)
        expected_text = helper.create_formatted_string(new_note_name, new_note_value, count_push_enter)
        note_names = [note.get_text() for note in list_notes_in_local_storage]
        assert_that(note_names).does_not_contain(expected_text)


