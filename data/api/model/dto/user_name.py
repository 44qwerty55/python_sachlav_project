class UserName:

    def __init__(self, firstname: str, lastname: str):
        self.__firstname = firstname
        self.__lastname = lastname

    def get_firstname(self) -> str:
        return self.__firstname

    def get_lastname(self) -> str:
        return self.__lastname

    def set_firstname(self, firstname: str):
        self.__firstname = firstname
        return self

    def set_lastname(self, lastname: str):
        self.__lastname = lastname
        return self

    def to_dict(self):
        return {
            "firstname": self.get_firstname(),
            "lastname": self.get_lastname()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            firstname=data.get('firstname'),
            lastname=data.get('lastname')
        )