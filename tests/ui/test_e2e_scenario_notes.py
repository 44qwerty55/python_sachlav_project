from data.ui.helpers import helper

count_push_enter = 3


def test_validate_new_note_in_preview_mode(note_page, generate_new_note_name, generate_new_note_value):
    note_page.create_new_node_node(generate_new_note_name, generate_new_note_value, count_push_enter)
    note_page.click_preview_mode_button()
    note_page.validate_node_in_preview(
        helper.create_formatted_string(generate_new_note_name, generate_new_note_value, count_push_enter))


def test_add_new_note_to_favorite(note_page, generate_new_note_name, generate_new_note_value):
    note_page.create_new_node_node(generate_new_note_name, generate_new_note_value, count_push_enter)
    note_page.click_add_note_to_favorite_button()
    note_page.click_favorite_button()
    note_page.validate_node_in_title(generate_new_note_name)


def test_delete_note(note_page, generate_new_note_name, generate_new_note_value):
    note_page.create_new_node_node(generate_new_note_name, generate_new_note_value, count_push_enter)
    note_page.validate_node_in_title(generate_new_note_name)
    note_page.click_delete_note_button()
    note_page.validate_not_node_in_title(generate_new_note_name)
    note_page.click_trash_button()
    note_page.validate_node_in_title(generate_new_note_name)
