class ProductForCard:

    def __init__(self, product_id: int, quantity: int):
        self.__product_id = product_id
        self.__quantity = quantity

    def get_product_id(self) -> int:
        return self.__product_id

    def get_quantity(self) -> int:
        return self.__quantity

    def set_product_id(self, product_id: int):
        self.__product_id = product_id
        return self

    def set_quantity(self, quantity: int):
        self.__quantity = quantity
        return self

    def to_dict(self):
        return {
            "productId": self.get_product_id(),
            "quantity": self.get_quantity()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data.get('productId'),
            quantity=data.get('quantity')
        )