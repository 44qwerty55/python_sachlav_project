from data.ui.constants.default_constance import NEW_CATEGORY_VALUE, NEW_VALUE

count_push_enter = 3


def test_create_new_category(main_page):
    main_page.push_new_category_button()
    main_page.type_new_category(NEW_CATEGORY_VALUE)
    main_page.validate_name_category(NEW_CATEGORY_VALUE[:20])

def test_delete_category(main_page):
    main_page.push_new_category_button()
    main_page.type_new_category(NEW_CATEGORY_VALUE)
    main_page.validate_name_category(NEW_CATEGORY_VALUE[:20])
    main_page.push_delete_category_button()
    main_page.validate_not_category_in_title(NEW_CATEGORY_VALUE[:20])

def test_rename_category(main_page):
    main_page.push_new_category_button()
    main_page.type_new_category(NEW_CATEGORY_VALUE)
    main_page.validate_name_category(NEW_CATEGORY_VALUE[:20])
    main_page.push_rename_category_button()
    main_page.type_rename_category(NEW_VALUE)
    main_page.validate_name_category(NEW_VALUE[:20])

