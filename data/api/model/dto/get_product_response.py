from data.api.model.product import Product
from data.api.model.dto.rating import Rating

class ProductResponse(Product):

    def __init__(self, id: int, title: str, price: float, description: str, category: str, image: str, rating: Rating):
        super().__init__(id, title, price, description, category, image)
        self.__rating = rating

    def get_rating(self) -> Rating:
        return self.__rating

    def set_rating(self, rating: Rating):
        self.__rating = rating
        return self

    def to_dict(self):
        return {
            "id": self.get_id(),
            "title": self.get_title(),
            "price": self.get_price(),
            "description": self.get_description(),
            "category": self.get_category(),
            "image": self.get_image(),
            "rating": self.__rating.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        rating_data = data.get('rating', {})
        rating = Rating.from_dict(rating_data)
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            price=data.get('price'),
            description=data.get('description'),
            category=data.get('category'),
            image=data.get('image'),
            rating=rating
        )
