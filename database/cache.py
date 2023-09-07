```python
import sqlite3
from db_ops import get_data, update_data

class Cache:
    def __init__(self, db_name):
        self.db_name = db_name
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            data = get_data(self.db_name, key)
            self.cache[key] = data
            return data

    def set(self, key, value):
        self.cache[key] = value
        update_data(self.db_name, key, value)

    def remove(self, key):
        if key in self.cache:
            del self.cache[key]
        update_data(self.db_name, key, None)

    def clear(self):
        self.cache.clear()

game_cache = Cache('game.db')
```