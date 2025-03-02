import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    @staticmethod
    def log_request(method: str, url: str, **kwargs):
        logging.info(f"Request: {method.upper()} {url} - Params: {kwargs.get('params')}, Data: {kwargs.get('json')}")

    @staticmethod
    def log_response(response):
        logging.info(f"Response: {response.status_code} - {response.json() if response.status_code == 200 else response.text}")
