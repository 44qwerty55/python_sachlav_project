from typing import List

from data.api.model.dto.product_from_card import ProductForCard


class Card():

    def __init__(self, id: int, user_id: int, products: List[ProductForCard]):
        self.__id = id
        self.__user_id = user_id
        self.__products = products

    def get_id(self) -> int:
        return self.__id

    def get_user_id(self) -> int:
        return self.__user_id

    def set_id(self, id: int):
        self.__id = id
        return self

    def set_user_id(self, user_id: int):
        self.__user_id = user_id
        return self

    def get_products(self) -> List[ProductForCard]:
        return self.__products

    def set_products(self, products: List[ProductForCard]):
        self.__products = products
        return self

    def add_product(self, product: ProductForCard):
        self.__products.append(product)

    def remove_product(self, product: ProductForCard):
        if product in self.__products:
            self.__products.remove(product)

    def to_dict(self):
        return {
            "id": self.get_id(),
            "userId": self.get_user_id(),
            "products": [product.to_dict() for product in self.__products]
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            user_id=data.get('userId'),
            products=[ProductForCard.from_dict(p) for p in data.get('products', [])]
        )
