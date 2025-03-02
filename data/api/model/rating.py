class Rating:

    def __init__(self, count: float, rate: float):
        self.__count = count
        self.__rate = rate

    def get_count(self) -> float:
        return self.__count

    def get_rate(self) -> float:
        return self.__rate

    def set_count(self, count: float):
        self.__count = count

    def set_rate(self, rate: float):
        self.__rate = rate

    def to_dict(self):
        return {
            "count": self.get_count(),
            "rate": self.get_rate()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            count=data.get('count'),
            rate=data.get('rate')
        )