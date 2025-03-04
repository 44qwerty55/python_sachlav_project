import uuid
import random

from data.api.model.card import Card
from data.api.model.dto.product_from_card import ProductForCard
from data.api.model.product import Product
from data.api.model.user import User


def create_new_user() -> User:
    username = f"username"
    email = "test@test.com"
    password = uuid.uuid4().hex
    return User(None, username, email, password)


def create_new_random_product() -> Product:
    title = f"title_product_{uuid.uuid4().hex}"
    price = round(random.uniform(0.0, 100.0), 2)
    description = f"description_{uuid.uuid4().hex}"
    category = f"category_{uuid.uuid4().hex}"
    image = "http://example.com"
    return Product(None, title, price, description, category, image)


def create_new_random_card(id: int) -> Card:
    random_quantity = random.randint(1, 100)
    products = ProductForCard(4, random_quantity)
    return Card(None, id, [products])
