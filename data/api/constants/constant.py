import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_USER = os.getenv("DEFAULT_USER")
DEFAULT_PASSWORD = os.getenv("DEFAULT_PASSWORD")

ANOTHER_VALUE =  "another value"
ANOTHER_EMAIL =  "anotheremail@test.com"