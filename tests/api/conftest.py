import json
import os

import allure
import pytest

from data.api.constants.constant import DEFAULT_PASSWORD, DEFAULT_USER
from data.api.constants.environment_urls import PRODUCTS, CARTS, USERS
from data.api.model.cart import Cart
from data.api.model.dto.get_cart_response import CartResponse
from data.api.model.dto.get_product_response import ProductResponse
from data.api.model.dto.get_user_response import UserResponse
from data.api.model.product import Product
from data.api.model.user import User
from data.api.requests.requests_builder import RequestsBuilder
from data.api.helpers import generator

current_dir = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
@allure.step("post new product")
def actual_post_user_response(request):
    user_request = request.param
    req_builder = RequestsBuilder(PRODUCTS)
    return req_builder.execute_post_request(user_request)


@pytest.fixture()
def new_random_product() -> Product:
    return generator.create_new_random_product()


@pytest.fixture()
def new_random_card(default_created_user) -> Cart:
    return generator.create_new_random_cart(default_created_user.get_id())


@pytest.fixture()
def new_random_user() -> User:
    return generator.create_new_user()


@pytest.fixture()
def create_random_product(new_random_product) -> Product:
    product = new_random_product
    actual_response = RequestsBuilder(PRODUCTS).execute_post_request(product.to_dict())
    product.set_id(actual_response.json()['id'])
    return product


@pytest.fixture()
def create_random_card(new_random_card) -> Cart:
    card = new_random_card
    actual_response = RequestsBuilder(CARTS).execute_post_request(card.to_dict())
    card.set_id(actual_response.json()['id'])
    return card


@pytest.fixture()
def create_random_user(new_random_user) -> User:
    user = new_random_user
    actual_response = RequestsBuilder(USERS).execute_post_request(user.to_dict())
    user.set_id(actual_response.json()['id'])
    return user


@pytest.fixture()
def default_created_product_response():
    file_path = os.path.join(current_dir, 'data_jsons/default_product_data.json')
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return ProductResponse.from_dict(data)


@pytest.fixture
def expected_products_response():
    file_path = os.path.join(current_dir, 'data_jsons/products_response_data.json')
    with open(file_path, "r", encoding='utf-8') as file:
        products = [ProductResponse.from_dict(product) for product in json.load(file)]
        return [product.to_dict() for product in products]


@pytest.fixture()
def default_created_card_response():
    file_path = os.path.join(current_dir, 'data_jsons/default_card_data.json')
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return CartResponse.from_dict(data)


@pytest.fixture
def expected_cards_response():
    file_path = os.path.join(current_dir, 'data_jsons/cards_response_data.json')
    with open(file_path, "r", encoding='utf-8') as file:
        cards = [CartResponse.from_dict(card) for card in json.load(file)]
        return [card.to_dict() for card in cards]


@pytest.fixture()
def default_created_user_response():
    file_path = os.path.join(current_dir, 'data_jsons/default_user_data.json')
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return UserResponse.from_dict(data)


@pytest.fixture
def expected_users_response():
    file_path = os.path.join(current_dir, 'data_jsons/users_response_data.json')
    with open(file_path, "r", encoding='utf-8') as file:
        users = [UserResponse.from_dict(user) for user in json.load(file)]
        return [user.to_dict() for user in users]


@pytest.fixture()
def default_created_user():
    user = User(1, DEFAULT_USER, "john@gmail.com", DEFAULT_PASSWORD)
    return user
