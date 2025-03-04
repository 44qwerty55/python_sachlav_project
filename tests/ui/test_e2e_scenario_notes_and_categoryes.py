
count_push_enter = 3


def test_move_to_category_menu(note_page, category_page, new_note_name, new_note_value, new_category_name):
    category_page.push_new_category_button()
    category_page.type_new_category(new_category_name)
    category_page.validate_name_category(new_category_name)
    note_page.create_new_node_node(new_note_name, new_note_value, count_push_enter)
    note_page.click_note_by_name(new_note_name)
    note_page.select_category_move_to_category_option_in_menu(new_category_name)
    category_page.category_list()
    note_page.validate_node_in_title(new_note_name)
