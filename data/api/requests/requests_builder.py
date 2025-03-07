import allure
import requests

from data.api.constants.http_metods import HttpMethod
from data.api.helpers.logger import Logger


class RequestsBuilder:

    def __init__(self, url: str):
        self.url = url

    def _execute_request(self, method: str, url: str, json=None):
        Logger.log_request(method, url)
        response = requests.request(method, url, json=json)
        Logger.log_response(response)

        allure.attach(url, "Request URL", allure.attachment_type.TEXT)
        allure.attach(response.text, "Response Body", allure.attachment_type.JSON)
        allure.attach(str(response.status_code), "Response Status Code", allure.attachment_type.TEXT)

        return response

    @allure.step("Send GET request")
    def execute_get_request(self):
        return self._execute_request(HttpMethod.GET.value, self.url)

    @allure.step("Send POST request")
    def execute_post_request(self, json=None):
        return self._execute_request(HttpMethod.POST.value, self.url, json)

    @allure.step("Send PUT request")
    def execute_put_request(self, id: str, json=None):
        full_url = f"{self.url}/{id}"
        return self._execute_request(HttpMethod.PUT.value, full_url, json)

    @allure.step("Send GET request by ID")
    def execute_get_request_by_id(self, id: str):
        full_url = f"{self.url}/{id}"
        return self._execute_request(HttpMethod.GET.value, full_url)

    @allure.step("Send DELETE request by ID")
    def execute_delete_request_by_id(self, id: str):
        full_url = f"{self.url}/{id}"
        return self._execute_request('delete', full_url)
