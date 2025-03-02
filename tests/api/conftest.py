import os
import uuid
from http import HTTPStatus
import random
import pytest
import json

from assertpy import assert_that

from data.api.constants.environment_urls import PRODUCTS
from data.api.model.product import Product
from data.api.model.get_product_response import ProductsResponse
from data.api.model.rating import Rating
from data.api.requests.requests_builder import RequestsBuilder

base_path = os.path.dirname(__file__)

@pytest.fixture
def actual_get_all_products_response():
    req_builder = RequestsBuilder(PRODUCTS)
    return req_builder.execute_get_request()

@pytest.fixture
def actual_post_user_response(request):
    user_request = request.param
    req_builder = RequestsBuilder(PRODUCTS)
    return req_builder.execute_post_request(user_request)

@pytest.fixture()
def created_new_random_product():
    title = f"title_product_{uuid.uuid4().hex}"
    price = round(random.uniform(0.0, 100.0), 2)
    description = f"description_{uuid.uuid4().hex}"
    category = f"category_{uuid.uuid4().hex}"
    image = "http://example.com"
    return Product(None, title, price, description, category, image)

@pytest.fixture()
def default_created_product():
    rating = Rating(120, 3.9)
    product = ProductsResponse(1, "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", 109.95, "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday", "men's clothing", "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg", rating)
    return product

@pytest.fixture
def expected_products_response():
    with open("data_jsons/products_response_data.json", "r", encoding='utf-8') as file_to_read:
        data_json_from_file = json.load(file_to_read)
        products = [ProductsResponse.from_dict(product) for product in data_json_from_file]
        expected_products_dicts = [product.to_dict() for product in products]
        return expected_products_dicts

