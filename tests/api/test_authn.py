from http import HTTPStatus

import allure
import pytest
from assertpy import assert_that

from data.api.constants.environment_urls import AUTHN
from data.api.model.login import Login
from data.api.requests.requests_builder import RequestsBuilder


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API authn")
def test_correct_authn(default_created_user):
    request = Login.instance(default_created_user)
    actual_response = RequestsBuilder(AUTHN).execute_post_request(request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(actual_response.json()["token"]).is_not_empty()
