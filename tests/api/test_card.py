from http import HTTPStatus

import allure
import pytest
from assertpy import assert_that

from data.api.constants.environment_urls import CARDS
from data.api.requests.requests_builder import RequestsBuilder


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API create new card test")
def test_correct_card_creation(new_random_card_dto):
    request = new_random_card_dto
    actual_response = RequestsBuilder(CARDS).execute_post_request(request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)

    request.set_id(11)
    assert_that(actual_response.json()).is_equal_to(request.to_dict())


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API update card test")
def test_correct_card_update(create_random_card):
    request = create_random_card.set_user_id(2)
    actual_response = RequestsBuilder(CARDS).execute_put_request(request.get_id(), request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(actual_response.json()).is_equal_to(request.to_dict())


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API get card by ID test")
def test_correct_get_card(default_created_card_response):
    actual_response = RequestsBuilder(CARDS).execute_get_request_by_id(default_created_card_response.get_id())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    actual_json = actual_response.json()
    assert_that(actual_json).is_equal_to(default_created_card_response.to_dict())


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
@allure.title("API get all cards test")
def test_correct_get_cards(expected_cards_response, default_created_card_response):
    actual_response = RequestsBuilder(CARDS).execute_get_request()
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    actual_json = actual_response.json()
    assert_that(actual_json).is_equal_to(expected_cards_response)
    assert_that(actual_json).contains(default_created_card_response.to_dict())
    assert_that(actual_json).is_length(7)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API delete card by ID test")
def test_correct_delete_card(default_created_card_response):
    actual_response = RequestsBuilder(CARDS).execute_delete_request_by_id(default_created_card_response.get_id())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    actual_json = actual_response.json()
    assert_that(actual_json).is_equal_to(default_created_card_response.to_dict())
