```python
import json
from pathlib import Path

class DnDContentAdapter:
    def __init__(self, content_file_path):
        self.content_file_path = Path(content_file_path)
        self.content_data = self.load_content_data()

    def load_content_data(self):
        if not self.content_file_path.exists():
            raise FileNotFoundError(f"The content file {self.content_file_path} does not exist.")
        with open(self.content_file_path, 'r') as file:
            return json.load(file)

    def get_content_by_category(self, category):
        return self.content_data.get(category, [])

    def add_new_content(self, category, content):
        if category not in self.content_data:
            self.content_data[category] = []
        self.content_data[category].append(content)
        self.save_content_data()

    def update_content(self, category, old_content, new_content):
        if category in self.content_data and old_content in self.content_data[category]:
            index = self.content_data[category].index(old_content)
            self.content_data[category][index] = new_content
            self.save_content_data()

    def delete_content(self, category, content):
        if category in self.content_data and content in self.content_data[category]:
            self.content_data[category].remove(content)
            self.save_content_data()

    def save_content_data(self):
        with open(self.content_file_path, 'w') as file:
            json.dump(self.content_data, file, indent=4)

# Example usage:
# content_adapter = DnDContentAdapter('path/to/dnd_content.json')
# content_adapter.add_new_content('spells', {'name': 'Fireball', 'level': 3})
# content_adapter.update_content('spells', {'name': 'Fireball', 'level': 3}, {'name': 'Fireball', 'level': 4})
# content_adapter.delete_content('spells', {'name': 'Fireball', 'level': 4})
```