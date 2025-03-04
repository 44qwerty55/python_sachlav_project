from typing import List

from data.api.model.card import Card
from data.api.model.dto.product_from_card import ProductForCard


class CardResponse(Card):

    def __init__(self, id: int, user_id: int, date: str, products: List[ProductForCard], version: int):
        super().__init__(id, user_id, products)
        self.__date = date
        self.__version = version

    def get_date(self) -> str:
        return self.__date

    def get_version(self) -> int:
        return self.__version

    def set_date(self, date: str):
        self.__date = date
        return self

    def set_version(self, version: int):
        self.__version = version
        return self

    def to_dict(self):
        return {
            "id": self.get_id(),
            "userId": self.get_user_id(),
            "date": self.get_date(),
            "products": [product.to_dict() for product in self.get_products()],
            "__v": self.get_version()
        }

    @classmethod
    def from_dict(cls, data):
        products_data = data.get("products", [])
        products = [ProductForCard.from_dict(p) for p in products_data]
        return cls(
            id=data.get('id'),
            user_id=data.get('userId'),
            date=data.get('date'),
            products=products,
            version=data.get('__v')
        )
