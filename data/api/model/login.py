from data.api.model.user import User


class Login:

    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def set_username(self, username: str):
        self.__username = username
        return self

    def set_password(self, password: str):
        self.__password = password
        return self

    def to_dict(self):
        return {
            "username": self.get_username(),
            "password": self.get_password()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data.get('username'),
            password=data.get('password')
        )

    @classmethod
    def instance(self, user: User):
        return  Login(user.get_username(), user.get_password())