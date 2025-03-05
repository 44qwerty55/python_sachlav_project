from typing import Optional, Dict

from data.ui.model.category import Category


class Note:
    def __init__(self, id: str, text: str, category: Optional[Category], scratchpad: bool, favorite: bool, created: str, last_updated: str):
        self.__id = id
        self.__text = text
        self.__category = category
        self.__scratchpad = scratchpad
        self.__favorite = favorite
        self.__created = created
        self.__last_updated = last_updated

    def get_id(self) -> str:
        return self.__id

    def get_text(self) -> str:
        return self.__text

    def get_category(self) -> Optional[Category]:
        return self.__category

    def get_scratchpad(self) -> bool:
        return self.__scratchpad

    def get_favorite(self) -> bool:
        return self.__favorite

    def get_created(self) -> str:
        return self.__created

    def get_last_updated(self) -> str:
        return self.__last_updated

    def set_id(self, id: str):
        self.__id = id
        return self

    def set_text(self, text: str):
        self.__text = text
        return self

    def set_category(self, category: Optional[Category]):
        self.__category = category
        return self

    def set_scratchpad(self, scratchpad: bool):
        self.__scratchpad = scratchpad
        return self

    def set_favorite(self, favorite: bool):
        self.__favorite = favorite
        return self

    def set_created(self, created: str):
        self.__created = created
        return self

    def set_last_updated(self, last_updated: str):
        self.__last_updated = last_updated
        return self

    def __repr__(self):
        return f"Note(id={self.get_id()}, text={self.get_text()[:30]}..., category={self.get_category()}, scratchpad={self.get_scratchpad()}, favorite={self.get_favorite()})"

    @classmethod
    def from_dict(cls, data: Dict, categories_dict: Dict[str, Category]) -> "Note":
        return cls(
            id=data["id"],
            text=data["text"],
            category=categories_dict.get(data.get("category"), None),
            scratchpad=data.get("scratchpad", False),
            favorite=data.get("favorite", False),
            created=data["created"],
            last_updated=data["lastUpdated"]
        )

    def to_dict(self) -> Dict:
        return {
            "id": self.get_id(),
            "text": self.get_text(),
            "category": self.get_category().to_dict() if self.get_category() else None,
            "scratchpad": self.get_scratchpad(),
            "favorite": self.get_favorite(),
            "created": self.get_created(),
            "lastUpdated": self.get_last_updated()
        }
