```python
import json
from pathlib import Path

class ContentManagementSystem:
    def __init__(self, content_file_path):
        self.content_file_path = Path(content_file_path)
        self.content_data = self.load_content_data()

    def load_content_data(self):
        if not self.content_file_path.exists():
            return {}
        with open(self.content_file_path, 'r') as file:
            return json.load(file)

    def save_content_data(self):
        with open(self.content_file_path, 'w') as file:
            json.dump(self.content_data, file, indent=4)

    def add_content(self, content_type, content):
        if content_type not in self.content_data:
            self.content_data[content_type] = []
        self.content_data[content_type].append(content)
        self.save_content_data()

    def update_content(self, content_type, content_id, new_content):
        if content_type in self.content_data:
            for index, content in enumerate(self.content_data[content_type]):
                if content['id'] == content_id:
                    self.content_data[content_type][index] = new_content
                    self.save_content_data()
                    return True
        return False

    def delete_content(self, content_type, content_id):
        if content_type in self.content_data:
            self.content_data[content_type] = [
                content for content in self.content_data[content_type]
                if content['id'] != content_id
            ]
            self.save_content_data()
            return True
        return False

    def get_content(self, content_type):
        return self.content_data.get(content_type, [])

# Example usage:
# cms = ContentManagementSystem('path_to_content.json')
# cms.add_content('quests', {'id': 1, 'name': 'Quest of the Ancient Sword', 'description': 'Retrieve the ancient sword of legends.'})
# cms.update_content('quests', 1, {'id': 1, 'name': 'Quest of the Ancient Sword', 'description': 'The sword has been stolen by a dragon!'})
# cms.delete_content('quests', 1)
# quests = cms.get_content('quests')
```