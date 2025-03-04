from data.api.model.dto.geolocation import Geolocation

class Address():

    def __init__(self, city: str, street: str, number: int, zipcode: str, geolocation: Geolocation):
        self.__city = city
        self.__street = street
        self.__number = number
        self.__zipcode = zipcode
        self.__geolocation = geolocation

    def get_city(self) -> str:
        return self.__city

    def get_street(self) -> str:
        return self.__street

    def get_number(self) -> int:
        return self.__number

    def get_zipcode(self) -> str:
        return self.__zipcode

    def get_geolocation(self) -> Geolocation:
        return self.__geolocation

    def set_city(self, city: str):
        self.__city = city
        return self

    def set_street(self, street: str):
        self.__street = street
        return self

    def set_number(self, number: int):
        self.__number = number
        return self

    def set_zipcode(self, zipcode: str):
        self.__zipcode = zipcode
        return self

    def set_geolocation(self, geolocation: Geolocation):
        self.__geolocation = geolocation
        return self

    def to_dict(self):
        return {
            "geolocation": self.get_geolocation().to_dict(),
            "city": self.get_city(),
            "street": self.get_street(),
            "number": self.get_number(),
            "zipcode": self.get_zipcode()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            geolocation=Geolocation.from_dict(data.get("geolocation", {})),
            city=data.get("city"),
            street=data.get("street"),
            number=data.get("number"),
            zipcode=data.get("zipcode")
        )
