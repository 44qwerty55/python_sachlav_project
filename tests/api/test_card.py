
import allure
import pytest

from data.api.constants.environment_urls import CARTS
from tests.api.base_api_class import BaseApiClass


class CardApiClass(BaseApiClass):
    ENDPOINT = CARTS

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API get card by ID test")
def test_correct_get_card(default_created_card_response):
    CardApiClass().get_request_by_id(default_created_card_response)

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
@allure.title("API get all cards test")
def test_correct_get_cards(expected_cards_response, default_created_card_response):
    CardApiClass().get_all_request(expected_cards_response, default_created_card_response, expected_length=7)

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API create new card test")
def test_correct_card_creation(new_random_card):
    CardApiClass().create_request(new_random_card, expected_id=11)

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API update card test")
def test_correct_card_update(create_random_card):
    request = create_random_card.set_user_id(2)
    CardApiClass().update_request(request)

@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API delete card by ID test")
def test_correct_delete_card(default_created_card_response):
    CardApiClass().delete_request(default_created_card_response)

