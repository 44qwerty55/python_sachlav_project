from data.ui.helpers import helper

count_push_enter = 3


def test_validate_new_note_in_preview_mode(main_page, generate_new_note_name, generate_new_note_value):
    main_page.create_new_node_node(generate_new_note_name, generate_new_note_value, count_push_enter)
    main_page.click_preview_mode_button()
    main_page.validate_node_in_preview(
        helper.create_formatted_string(generate_new_note_name, generate_new_note_value, count_push_enter))


def test_add_new_note_to_favorite(main_page, generate_new_note_name, generate_new_note_value):
    main_page.create_new_node_node(generate_new_note_name, generate_new_note_value, count_push_enter)
    main_page.click_add_note_to_favorite_button()
    main_page.click_favorite_button()
    main_page.validate_node_in_title(generate_new_note_name)


def test_delete_note(main_page, generate_new_note_name, generate_new_note_value):
    main_page.create_new_node_node(generate_new_note_name, generate_new_note_value, count_push_enter)
    main_page.validate_node_in_title(generate_new_note_name)
    main_page.click_delete_note_button()
    main_page.validate_not_node_in_title(generate_new_note_name)
    main_page.click_trash_button()
    main_page.validate_node_in_title(generate_new_note_name)
