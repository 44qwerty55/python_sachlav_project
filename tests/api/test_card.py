
import allure
import pytest

from data.api.constants.environment_urls import CARDS
from tests.api.base_api_test import BaseApiTest


class CardApiTest(BaseApiTest):
    ENDPOINT = CARDS

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API get card by ID test")
def test_correct_get_card(default_created_card_response):
    CardApiTest().get_request_by_id(default_created_card_response)

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
@allure.title("API get all cards test")
def test_correct_get_cards(expected_cards_response, default_created_card_response):
    CardApiTest().get_all_request(expected_cards_response, default_created_card_response, expected_length=7)

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API create new card test")
def test_correct_card_creation(new_random_card):
    CardApiTest().create_request(new_random_card, expected_id=11)

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API update card test")
def test_correct_card_update(create_random_card):
    request = create_random_card.set_user_id(2)
    CardApiTest().update_request(request)

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API delete card by ID test")
def test_correct_delete_card(default_created_card_response):
    CardApiTest().delete_request(default_created_card_response)

