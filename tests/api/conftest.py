import json
import os
import random
import uuid

import allure
import pytest

from data.api.constants.environment_urls import PRODUCTS, CARDS, USERS
from data.api.model.card import Card
from data.api.model.dto.get_card_response import CardResponse
from data.api.model.dto.get_product_response import ProductResponse
from data.api.model.dto.get_user_response import UserResponse
from data.api.model.product import Product
from data.api.model.dto.product_from_card import ProductForCard
from data.api.model.user import User
from data.api.requests.requests_builder import RequestsBuilder

current_dir = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
@allure.step("post new product")
def actual_post_user_response(request):
    user_request = request.param
    req_builder = RequestsBuilder(PRODUCTS)
    return req_builder.execute_post_request(user_request)


@pytest.fixture()
def new_random_product_dto() -> Product:
    title = f"title_product_{uuid.uuid4().hex}"
    price = round(random.uniform(0.0, 100.0), 2)
    description = f"description_{uuid.uuid4().hex}"
    category = f"category_{uuid.uuid4().hex}"
    image = "http://example.com"
    return Product(None, title, price, description, category, image)

@pytest.fixture()
def new_random_card_dto(default_created_user) -> Card:
    user_id = default_created_user.get_id()
    random_quantity = random.randint(1, 100)
    products = ProductForCard(4, random_quantity)
    return Card(None, user_id, [products])

@pytest.fixture()
def new_random_user_dto() -> User:
    username = f"username"
    email = "test@test.com"
    password = uuid.uuid4().hex
    return User(None, username, email, password)

@pytest.fixture()
def create_random_product(new_random_product_dto) -> Product:
    product = new_random_product_dto
    actual_response = RequestsBuilder(PRODUCTS).execute_post_request(product.to_dict())
    product.set_id(actual_response.json()['id'])
    return product

@pytest.fixture()
def create_random_card(new_random_card_dto) -> Card:
    card = new_random_card_dto
    actual_response = RequestsBuilder(CARDS).execute_post_request(card.to_dict())
    card.set_id(actual_response.json()['id'])
    return card

@pytest.fixture()
def create_random_user(new_random_user_dto) -> User:
    user = new_random_user_dto
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
        return CardResponse.from_dict(data)

@pytest.fixture
def expected_cards_response():
    file_path = os.path.join(current_dir, 'data_jsons/cards_response_data.json')
    with open(file_path, "r", encoding='utf-8') as file:
        cards = [CardResponse.from_dict(card) for card in json.load(file)]
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
    user = User(1, "johnd", "john@gmail.com", "m38rmF$")
    return user


