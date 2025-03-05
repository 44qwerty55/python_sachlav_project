import json

import allure
import pytest

from data.ui.helpers import helper

count_push_enter = 3

@pytest.mark.positive
@pytest.mark.ui
@allure.severity(allure.severity_level.NORMAL)
@allure.title("UI create new note and view in preview mode test")
def test_validate_new_note_in_preview_mode(note_page, new_note_name, new_note_value):
    note_page.create_new_node_node(new_note_name, new_note_value, count_push_enter)
    note_page.click_preview_mode_button()
    note_page.validate_node_in_preview(
        helper.create_formatted_string(new_note_name, new_note_value, count_push_enter))

@pytest.mark.positive
@pytest.mark.ui
@allure.severity(allure.severity_level.NORMAL)
@allure.title("UI add note to favorite test")
def test_add_new_note_to_favorite(note_page, new_note_name, new_note_value):
    note_page.create_new_node_node(new_note_name, new_note_value, count_push_enter)
    note_page.click_add_note_to_favorite_button()
    note_page.click_favorite_button()
    note_page.validate_node_in_title(new_note_name)

@pytest.mark.positive
@pytest.mark.ui
@allure.severity(allure.severity_level.NORMAL)
@allure.title("UI add note to trash test")
def test_delete_note(note_page, new_note_name, new_note_value):
    note_page.create_new_node_node(new_note_name, new_note_value, count_push_enter)
    note_page.validate_node_in_title(new_note_name)
    note_page.click_delete_note_button()
    note_page.validate_not_node_in_title(new_note_name)
    note_page.click_trash_button()
    note_page.validate_node_in_title(new_note_name)

@pytest.mark.positive
@pytest.mark.ui
@allure.severity(allure.severity_level.NORMAL)
@allure.title("UI add text to scratchpad test")
def test_validate_new_note_in_scratchpad(note_page, new_note_name, new_note_value):
    note_page.click_scratchpad_button()
    note_page.write_value_in_node(new_note_value)
    note_page.click_preview_mode_button()
    note_page.validate_node_in_preview(new_note_value)

@pytest.mark.positive
@pytest.mark.ui
@allure.severity(allure.severity_level.NORMAL)
@allure.title("UI add note to favorite from menu test")
def test_add_new_note_to_favorite_from_menu(note_page, new_note_name, new_note_value):
    note_page.create_new_node_node(new_note_name, new_note_value, count_push_enter)
    note_page.click_note_by_name(new_note_name)
    note_page.click_favorite_option_in_menu()
    note_page.click_favorite_button()
    note_page.validate_node_in_title(new_note_name)

@pytest.mark.positive
@pytest.mark.ui
@allure.severity(allure.severity_level.NORMAL)
@allure.title("UI add note to trash from menu test")
def test_delete_from_menu(note_page, new_note_name, new_note_value):
    note_page.create_new_node_node(new_note_name, new_note_value, count_push_enter)
    note_page.click_note_by_name(new_note_name)
    note_page.click_trash_option_in_menu()
    note_page.validate_not_node_in_title(new_note_name)
    note_page.click_trash_button()
    note_page.validate_node_in_title(new_note_name)
