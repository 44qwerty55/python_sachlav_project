from data.api.model.dto.address import Address
from data.api.model.dto.user_name import UserName
from data.api.model.user import User


class UserResponse(User):

    def __init__(self, address: Address, id: int, username: str, email: str, password: str, user_name: UserName, phone: str, version: str):
        super().__init__(id, username, email, password)
        self.__address = address
        self.__user_name = user_name
        self.__phone = phone
        self.__version = version

    def get_address(self) -> Address:
        return self.__address

    def get_user_name(self) -> UserName:
        return self.__user_name

    def get_phone(self) -> str:
        return self.__phone

    def get_version(self) -> str:
        return self.__version

    def set_address(self, address: Address):
        self.__address = address
        return self

    def set_user_name(self, user_name: UserName):
        self.__user_name = user_name
        return self

    def set_phone(self, phone: str):
        self.__phone = phone
        return self

    def set_version(self, version: str):
        self.__version = version
        return self

    def to_dict(self):
        return {
            "address": self.get_address().to_dict(),
            "id": self.get_id(),
            "email": self.get_email(),
            "username": self.get_username(),
            "password": self.get_password(),
            "name": self.get_user_name().to_dict(),
            "phone": self.get_phone(),
            "__v": self.get_version()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            address=Address.from_dict(data.get("address", {})),
            id=data.get("id"),
            email=data.get("email"),
            username=data.get("username"),
            password=data.get("password"),
            user_name=UserName.from_dict(data.get("name", {})),
            phone=data.get("phone"),
            version=data.get("__v")
        )
