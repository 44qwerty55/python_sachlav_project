import json


class User:

    def __init__(self, id: int, username: str, email: str, password: str):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__password = password

    def get_id(self) -> int:
        return self.__id

    def get_username(self) -> str:
        return self.__username

    def get_email(self) -> str:
        return self.__email

    def get_password(self) -> str:
        return self.__password

    def set_id(self, id: int):
        self.__id = id
        return self

    def set_username(self, username: str):
        self.__username = username
        return self

    def set_email(self, email: str):
        self.__email = email
        return self

    def set_password(self, password: str):
        self.__password = password
        return self

    def to_dict(self):
        return {
            "id": self.get_id(),
            "username": self.get_username(),
            "email": self.get_email(),
            "password": self.get_password()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )
