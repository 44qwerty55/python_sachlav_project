import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL_API = os.getenv("BASE_URL_API")
PRODUCTS = f"{BASE_URL_API}/products"
CARDS =  f"{BASE_URL_API}/carts"
USERS =  f"{BASE_URL_API}/users"
AUTHN =  f"{BASE_URL_API}/auth/login"