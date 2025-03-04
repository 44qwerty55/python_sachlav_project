from data.ui.constants.default_constance import NEW_CATEGORY_VALUE, NEW_VALUE

count_push_enter = 3


def test_create_new_category(category_page):
    category_page.push_new_category_button()
    category_page.type_new_category(NEW_CATEGORY_VALUE)
    category_page.validate_name_category(NEW_CATEGORY_VALUE[:20])

def test_delete_category(category_page):
    category_page.push_new_category_button()
    category_page.type_new_category(NEW_CATEGORY_VALUE)
    category_page.validate_name_category(NEW_CATEGORY_VALUE[:20])
    category_page.push_delete_category_button()
    category_page.validate_not_category_in_title(NEW_CATEGORY_VALUE[:20])

def test_rename_category(category_page):
    category_page.push_new_category_button()
    category_page.type_new_category(NEW_CATEGORY_VALUE)
    category_page.validate_name_category(NEW_CATEGORY_VALUE[:20])
    category_page.push_rename_category_button()
    category_page.type_rename_category(NEW_VALUE)
    category_page.validate_name_category(NEW_VALUE[:20])

