from typing import Dict


class Category:
    def __init__(self, id: str, name: str, dragged_over: bool):
        self.__id = id
        self.__name = name
        self.__dragged_over = dragged_over

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_dragged_over(self) -> bool:
        return self.__dragged_over

    def set_id(self, id: str):
        self.__id = id
        return self

    def set_name(self, name: str):
        self.__name = name
        return self

    def set_dragged_over(self, dragged_over: bool):
        self.__dragged_over = dragged_over
        return self

    def __repr__(self):
        return f"Category(id={self.get_id()}, name={self.get_name()}, draggedOver={self.get_dragged_over()})"

    @classmethod
    def from_dict(cls, data: Dict) -> "Category":
        return cls(
            id=data["id"],
            name=data["name"],
            dragged_over=data["draggedOver"]
        )

    def to_dict(self) -> Dict:
        return {
            "id": self.get_id(),
            "name": self.get_name(),
            "draggedOver": self.get_dragged_over()
        }
