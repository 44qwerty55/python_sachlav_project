from http import HTTPStatus

from assertpy import assert_that

from data.api.constants.environment_urls import PRODUCTS
from data.api.requests.requests_builder import RequestsBuilder


def test_user_creation(created_new_random_product):
    request = created_new_random_product
    actual_response = RequestsBuilder(PRODUCTS).execute_post_request(request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)

    request.set_id(21)
    assert_that(actual_response.json()).is_equal_to(request.to_dict())

