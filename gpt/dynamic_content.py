```python
import json
from database import db_ops

class DynamicContent:
    def __init__(self):
        self.content = {}

    def load_content(self):
        self.content = db_ops.retrieve_all_content()

    def save_content(self):
        db_ops.save_all_content(self.content)

    def add_content(self, content_type, content_id, content_data):
        if content_type not in self.content:
            self.content[content_type] = {}
        self.content[content_type][content_id] = content_data
        self.save_content()

    def get_content(self, content_type, content_id):
        if content_type in self.content and content_id in self.content[content_type]:
            return self.content[content_type][content_id]
        else:
            return None

dynamic_content = DynamicContent()
```