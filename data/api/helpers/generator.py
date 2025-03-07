import uuid
import random

from data.api.model.cart import Cart
from data.api.model.dto.product_from_cart import ProductForCart
from data.api.model.product import Product
from data.api.model.user import User


def create_new_user() -> User:
    username = f"username"
    email = "test@test.com"
    password = uuid.uuid4().hex
    return User(id=None, username=username, email=email, password=password)


def create_new_random_product() -> Product:
    title = f"title_product_{uuid.uuid4().hex}"
    price = round(random.uniform(0.0, 100.0), 2)
    description = f"description_{uuid.uuid4().hex}"
    category = f"category_{uuid.uuid4().hex}"
    image = "http://example.com"
    return Product(id=None, title=title, price=price, description=description, category=category, image=image)


def create_new_random_cart(id: int) -> Cart:
    random_quantity = random.randint(1, 100)
    products = ProductForCart(4, random_quantity)
    return Cart(id=None, user_id=id, products=[products])
