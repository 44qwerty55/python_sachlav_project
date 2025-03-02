from http import HTTPStatus

from assertpy import assert_that

from data.api.model.get_product_response import ProductsResponse


def test_correct_get_products(actual_get_all_products_response, expected_products_response, default_created_product):
    assert_that(actual_get_all_products_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(actual_get_all_products_response.json()).is_equal_to(expected_products_response)
    assert_that(actual_get_all_products_response.json()).contains(default_created_product.to_dict())