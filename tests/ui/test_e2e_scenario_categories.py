from data.ui.constants.default_constance import NEW_CATEGORY_VALUE

count_push_enter = 3


def test_create_new_category(main_page):
    main_page.push_new_category_button()
    main_page.type_new_category(NEW_CATEGORY_VALUE)
    main_page.validate_new_category(NEW_CATEGORY_VALUE[:20])
