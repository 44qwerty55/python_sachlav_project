import json


class Product:

    def __init__(self, id: int, title: str, price: float, description: str, category: str, image: str):
        self.__id = id
        self.__title = title
        self.__price = price
        self.__description = description
        self.__category = category
        self.__image = image

    def get_id(self) -> int:
        return self.__id

    def get_title(self) -> str:
        return self.__title

    def get_price(self) -> float:
        return self.__price

    def get_description(self) -> str:
        return self.__description

    def get_category(self) -> str:
        return self.__category

    def get_image(self) -> str:
        return self.__image

    def set_id(self, id: int):
        self.__id = id
        return self

    def set_title(self, title: str):
        self.__title = title
        return self

    def set_price(self, price: float):
        self.__price = price
        return self

    def set_category(self, category: str):
        self.__category = category
        return self

    def set_description(self, description: str):
        self.__description = description
        return self

    def set_image(self, image: str):
        self.__image = image
        return self

    def to_dict(self):
        return {
            "id": self.get_id(),
            "title": self.get_title(),
            "price": self.get_price(),
            "description": self.get_description(),
            "category": self.get_category(),
            "image": self.get_image()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            price=data.get('price'),
            description=data.get('description'),
            category=data.get('category'),
            image=data.get('image')
        )
