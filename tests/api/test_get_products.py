from http import HTTPStatus

from assertpy import assert_that

def test_correct_get_products(actual_get_all_products_response, expected_products_response, default_created_product):
    assert_that(actual_get_all_products_response.status_code).is_equal_to(HTTPStatus.OK)
    actual = actual_get_all_products_response.json()
    assert_that(actual).is_equal_to(expected_products_response)
    assert_that(actual).contains(default_created_product.to_dict())
    assert_that(actual).is_length(20)