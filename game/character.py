```python
import json
from database import db_ops
from utils import error_handlers

class Character:
    def __init__(self, character_id):
        self.character_id = character_id
        self.character_data = self.load_character_data()

    def load_character_data(self):
        try:
            character_data = db_ops.get_character(self.character_id)
            return character_data
        except Exception as e:
            error_handlers.handle_error(e)

    def update_character_data(self, new_data):
        try:
            self.character_data.update(new_data)
            db_ops.update_character(self.character_id, self.character_data)
        except Exception as e:
            error_handlers.handle_error(e)

    def get_stat(self, stat_name):
        try:
            return self.character_data['stats'][stat_name]
        except KeyError:
            error_handlers.handle_error(f"Stat {stat_name} not found")

    def update_stat(self, stat_name, new_value):
        try:
            self.character_data['stats'][stat_name] = new_value
            self.update_character_data(self.character_data)
        except KeyError:
            error_handlers.handle_error(f"Stat {stat_name} not found")

    def get_inventory(self):
        return self.character_data['inventory']

    def add_to_inventory(self, item):
        self.character_data['inventory'].append(item)
        self.update_character_data(self.character_data)

    def remove_from_inventory(self, item):
        try:
            self.character_data['inventory'].remove(item)
            self.update_character_data(self.character_data)
        except ValueError:
            error_handlers.handle_error(f"Item {item} not found in inventory")
```