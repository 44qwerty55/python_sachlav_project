import json
from typing import List, Tuple, Optional

from data.ui.model.category import Category
from data.ui.model.note import Note


class LocalStorageHelper:

    @staticmethod
    def parse_categories(local_storage_data: str) -> List[Category]:
        data = json.loads(local_storage_data)
        categories_data = json.loads(data.get("categories", "[]"))
        return [Category.from_dict(c) for c in categories_data]

    @staticmethod
    def parse_notes(local_storage_data: str) -> List[Note]:
        data = json.loads(local_storage_data)
        categories_list = LocalStorageHelper.parse_categories(local_storage_data)
        categories_dict = {c.get_id(): c for c in categories_list}
        notes_data = json.loads(data.get("notes", "[]"))
        return [Note.from_dict(n, categories_dict) for n in notes_data]

    @staticmethod
    def parse_local_storage(local_storage_data: str) -> Tuple[List[Category], List[Note]]:
        categories = LocalStorageHelper.parse_categories(local_storage_data)
        notes = LocalStorageHelper.parse_notes(local_storage_data)
        return categories, notes

    @staticmethod
    def get_note_by_name(local_storage_data: str, note_name: str) -> Optional[Note]:
        notes = LocalStorageHelper.parse_notes(local_storage_data)
        matching_notes = [note for note in notes if note.get_text().startswith(note_name)]

        if len(matching_notes) > 1:
            raise ValueError(f"Found several notes with the name '{note_name}': {len(matching_notes)}")

        return matching_notes[0] if matching_notes else None

    @staticmethod
    def get_category_by_name(local_storage_data: str, category_name: str) -> Optional[Category]:
        categories = LocalStorageHelper.parse_categories(local_storage_data)
        for category in categories:
            if category.get_name() == category_name:
                return category
        return None