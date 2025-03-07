import allure
import pytest

from data.api.constants.constant import ANOTHER_EMAIL
from data.api.constants.environment_urls import USERS
from tests.api.base_api_class import BaseApiClass


class UserApiClass(BaseApiClass):
    ENDPOINT = USERS


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API create new user test")
@pytest.mark.skip(reason="The request result does not comply with the requirements")
@allure.link("https://fakestoreapi.com/docs#tag/Users/operation/addUser")
def test_correct_user_creation(new_random_user):
    UserApiClass().create_request(new_random_user, expected_id=11)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API update user test")
def test_correct_user_update(create_random_user):
    request = create_random_user.set_email(ANOTHER_EMAIL)
    UserApiClass().update_request(request)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API get user by ID test")
def test_correct_get_user(default_created_user_response):
    UserApiClass().get_request_by_id(default_created_user_response)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
@allure.title("API get all users test")
def test_correct_get_users(expected_users_response, default_created_user_response):
    UserApiClass().get_all_request(expected_users_response, default_created_user_response, expected_length=10)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API delete user by ID test")
def test_correct_delete_user(default_created_user_response):
    UserApiClass().delete_request(default_created_user_response)
