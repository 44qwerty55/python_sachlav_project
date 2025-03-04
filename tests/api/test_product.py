from http import HTTPStatus

import allure
import pytest
from assertpy import assert_that

from data.api.constants.constant import ANOTHER_VALUE
from data.api.constants.environment_urls import PRODUCTS
from data.api.requests.requests_builder import RequestsBuilder


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API create new product test")
def test_correct_product_creation(new_random_product_dto):
    request = new_random_product_dto
    actual_response = RequestsBuilder(PRODUCTS).execute_post_request(request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)

    request.set_id(21)
    assert_that(actual_response.json()).is_equal_to(request.to_dict())


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API update product test")
def test_correct_product_update(create_random_product):
    request = create_random_product.set_description(ANOTHER_VALUE)
    actual_response = RequestsBuilder(PRODUCTS).execute_put_request(request.get_id(), request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(actual_response.json()).is_equal_to(request.to_dict())


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API get product by ID test")
def test_correct_get_product(default_created_product_response):
    actual_response = RequestsBuilder(PRODUCTS).execute_get_request_by_id(default_created_product_response.get_id())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    actual_json = actual_response.json()
    assert_that(actual_json).is_equal_to(default_created_product_response.to_dict())


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
@allure.title("API get all products test")
def test_correct_get_products(expected_products_response, default_created_product_response):
    actual_response = RequestsBuilder(PRODUCTS).execute_get_request()
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    actual_json = actual_response.json()
    assert_that(actual_json).is_equal_to(expected_products_response)
    assert_that(actual_json).contains(default_created_product_response.to_dict())
    assert_that(actual_json).is_length(20)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API delete product by ID test")
def test_correct_delete_product(default_created_product_response):
    actual_response = RequestsBuilder(PRODUCTS).execute_delete_request_by_id(default_created_product_response.get_id())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    actual_json = actual_response.json()
    assert_that(actual_json).is_equal_to(default_created_product_response.to_dict())
