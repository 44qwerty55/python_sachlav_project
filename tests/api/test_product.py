import allure
import pytest

from data.api.constants.constant import ANOTHER_VALUE
from data.api.constants.environment_urls import PRODUCTS
from tests.api.base_api_test import BaseApiTest


class ProductApiTest(BaseApiTest):
    ENDPOINT = PRODUCTS


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API create new product test")
def test_correct_product_creation(new_random_product):
    ProductApiTest().create_request(new_random_product, expected_id=21)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API update product test")
def test_correct_product_update(create_random_product):
    request = create_random_product.set_description(ANOTHER_VALUE)
    ProductApiTest().update_request(request)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API get product by ID test")
def test_correct_get_product(default_created_product_response):
    ProductApiTest().get_request_by_id(default_created_product_response)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
@allure.title("API get all products test")
def test_correct_get_products(expected_products_response, default_created_product_response):
    ProductApiTest().get_all_request(expected_products_response, default_created_product_response, expected_length=20)


@pytest.mark.positive
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API delete product by ID test")
def test_correct_delete_product(default_created_product_response):
    ProductApiTest().delete_request(default_created_product_response)
