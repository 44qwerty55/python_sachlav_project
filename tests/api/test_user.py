from http import HTTPStatus

import allure
import pytest
from assertpy import assert_that

from data.api.constants.constant import ANOTHER_EMAIL
from data.api.constants.environment_urls import PRODUCTS, USERS
from data.api.requests.requests_builder import RequestsBuilder


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API create new user test")
def test_correct_user_creation(new_random_user_dto):
    request = new_random_user_dto
    actual_response = RequestsBuilder(USERS).execute_post_request(request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)

    request.set_id(11)
    assert_that(actual_response.json()).is_equal_to(request.to_dict())


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API update user test")
def test_correct_user_update(create_random_user):
    request = create_random_user.set_email(ANOTHER_EMAIL)
    actual_response = RequestsBuilder(USERS).execute_put_request(request.get_id(), request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(actual_response.json()).is_equal_to(request.to_dict())


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API get user by ID test")
def test_correct_get_user(default_created_user_response):
    actual_response = RequestsBuilder(USERS).execute_get_request_by_id(default_created_user_response.get_id())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    actual_json = actual_response.json()
    assert_that(actual_json).is_equal_to(default_created_user_response.to_dict())


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
@allure.title("API get all users test")
def test_correct_get_users(expected_users_response, default_created_user_response):
    actual_response = RequestsBuilder(USERS).execute_get_request()
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    actual_json = actual_response.json()
    assert_that(actual_json).is_equal_to(expected_users_response)
    print(default_created_user_response.to_dict())
    assert_that(actual_json).contains(default_created_user_response.to_dict())
    assert_that(actual_json).is_length(10)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API delete user by ID test")
def test_correct_delete_user(default_created_user_response):
    actual_response = RequestsBuilder(USERS).execute_delete_request_by_id(default_created_user_response.get_id())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    actual_json = actual_response.json()
    assert_that(actual_json).is_equal_to(default_created_user_response.to_dict())
