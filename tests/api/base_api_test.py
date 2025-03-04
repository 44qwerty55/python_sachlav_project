
from http import HTTPStatus
from assertpy import assert_that

from data.api.requests.requests_builder import RequestsBuilder


class BaseApiTest:
    ENDPOINT = None

    def get_request_by_id(self, default_response):
        actual_response = RequestsBuilder(self.ENDPOINT).execute_get_request_by_id(default_response.get_id())
        assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
        actual_json = actual_response.json()
        assert_that(actual_json).is_equal_to(default_response.to_dict())

    def get_all_request(self, expected_response, default_response, expected_length):
        actual_response = RequestsBuilder(self.ENDPOINT).execute_get_request()
        assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
        actual_json = actual_response.json()
        assert_that(actual_json).is_equal_to(expected_response)
        assert_that(actual_json).contains(default_response.to_dict())
        assert_that(actual_json).is_length(expected_length)

    def create_request(self, new_object, expected_id):
        actual_response = RequestsBuilder(self.ENDPOINT).execute_post_request(new_object.to_dict())
        assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
        new_object.set_id(expected_id)
        assert_that(actual_response.json()).is_equal_to(new_object.to_dict())

    def update_request(self, request):
        actual_response = RequestsBuilder(self.ENDPOINT).execute_put_request(request.get_id(), request.to_dict())
        assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
        assert_that(actual_response.json()).is_equal_to(request.to_dict())

    def delete_request(self, default_response):
        actual_response = RequestsBuilder(self.ENDPOINT).execute_delete_request_by_id(default_response.get_id())
        assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
        actual_json = actual_response.json()
        assert_that(actual_json).is_equal_to(default_response.to_dict())