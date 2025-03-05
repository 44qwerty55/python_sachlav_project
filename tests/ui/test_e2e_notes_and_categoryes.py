

from assertpy import assert_that

from data.ui.helpers.local_storage_helper import LocalStorageHelper
from data.ui.pages.local_storage import LocalStorage

count_push_enter = 3


def test_move_to_category_menu(note_page, category_page, new_note_name, new_note_value, new_category_name):
    category_page.create_new_category(new_category_name)
    note_page.create_new_node_node(new_note_name, new_note_value, count_push_enter)
    note_page.click_note_by_name(new_note_name)
    note_page.select_category_move_to_category_option_in_menu(new_category_name)
    category_page.clic_to_category_list()
    note_page.validate_node_in_title(new_note_name)
    note_page.click_sync_button()

    local_storage = LocalStorage(note_page.page)
    storage_data = local_storage.get_local_storage()
    note_in_local_storage = LocalStorageHelper.get_note_by_name(storage_data, new_note_name)
    assert_that(note_in_local_storage.get_text()).starts_with(new_note_name)

