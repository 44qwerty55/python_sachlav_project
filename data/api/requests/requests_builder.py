import requests

from data.api.helpers.logger import Logger


class RequestsBuilder:

    def __init__(self, url: str):
        self.url = url

    def execute_get_request(self):
        Logger.log_request('get', self.url)
        response = requests.get(self.url)
        Logger.log_response(response)
        return response

    def execute_post_request(self, json=None):
        Logger.log_request('post', self.url)
        response = requests.post(self.url, json)
        Logger.log_response(response)
        return response

    def execute_put_request(self, json=None):
        Logger.log_request('post', self.url)
        response = requests.put(self.url, json)
        Logger.log_response(response)
        return response

    def execute_delete_request(self):
        Logger.log_request('delete', self.url)
        response = requests.delete(self.url)
        Logger.log_response(response)
        return response
