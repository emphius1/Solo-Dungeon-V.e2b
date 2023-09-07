```python
import json

class Settings:
    def __init__(self):
        self.settings_file = "settings.json"
        self.default_settings = {
            "volume": 100,
            "difficulty": "normal",
            "language": "English",
            "content_filter": "PG-13"
        }
        self.load_settings()

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            self.settings = self.default_settings
            self.save_settings()

    def save_settings(self):
        with open(self.settings_file, 'w') as file:
            json.dump(self.settings, file)

    def get_setting(self, setting_key):
        return self.settings.get(setting_key, None)

    def set_setting(self, setting_key, setting_value):
        self.settings[setting_key] = setting_value
        self.save_settings()

    def reset_to_defaults(self):
        self.settings = self.default_settings
        self.save_settings()
```