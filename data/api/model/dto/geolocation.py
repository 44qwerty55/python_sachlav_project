class Geolocation:

    def __init__(self, lat: str, long: str):
        self.__lat = lat
        self.__long = long

    def get_lat(self) -> str:
        return self.__lat

    def get_long(self) -> str:
        return self.__long

    def set_lat(self, lat: str):
        self.__lat = lat
        return self

    def set_long(self, long: str):
        self.__long = long
        return self

    def to_dict(self):
        return {
            "lat": self.get_lat(),
            "long": self.get_long()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            lat=data.get('lat'),
            long=data.get('long')
        )