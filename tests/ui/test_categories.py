from data.ui.constants.default_constance import  NEW_VALUE

count_push_enter = 3


def test_create_new_category(category_page, new_category_name):
    category_page.push_new_category_button()
    category_page.type_new_category(new_category_name)
    category_page.validate_name_category(new_category_name)


def test_delete_category(category_page, new_category_name):
    category_page.push_new_category_button()
    category_page.type_new_category(new_category_name)
    category_page.validate_name_category(new_category_name)
    category_page.push_delete_category_button(new_category_name)
    category_page.validate_not_category_in_title(new_category_name)


def test_rename_category(category_page, new_category_name):
    category_page.push_new_category_button()
    category_page.type_new_category(new_category_name)
    category_page.validate_name_category(new_category_name)
    category_page.push_rename_category_button(new_category_name)
    category_page.type_rename_category(NEW_VALUE)
    category_page.validate_name_category(NEW_VALUE)
