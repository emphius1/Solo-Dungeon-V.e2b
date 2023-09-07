```python
import os
import json
from utils.error_handlers import handle_mod_errors

class ModSupport:
    def __init__(self):
        self.mod_directory = "./mods/"
        self.mods = {}

    def load_mods(self):
        """Load all mods from the mod directory"""
        for filename in os.listdir(self.mod_directory):
            if filename.endswith(".json"):
                with open(os.path.join(self.mod_directory, filename), 'r') as f:
                    mod_data = json.load(f)
                    self.mods[mod_data['name']] = mod_data

    def apply_mods(self, game_data):
        """Apply all loaded mods to the game data"""
        for mod in self.mods.values():
            game_data = self.apply_mod(game_data, mod)
        return game_data

    @handle_mod_errors
    def apply_mod(self, game_data, mod):
        """Apply a single mod to the game data"""
        for action, value in mod['actions'].items():
            if action == 'add':
                game_data = self.add_to_game_data(game_data, value)
            elif action == 'remove':
                game_data = self.remove_from_game_data(game_data, value)
            elif action == 'replace':
                game_data = self.replace_in_game_data(game_data, value)
        return game_data

    def add_to_game_data(self, game_data, value):
        """Add new content to the game data"""
        for key, content in value.items():
            if key in game_data:
                game_data[key].extend(content)
            else:
                game_data[key] = content
        return game_data

    def remove_from_game_data(self, game_data, value):
        """Remove content from the game data"""
        for key, content in value.items():
            if key in game_data:
                game_data[key] = [item for item in game_data[key] if item not in content]
        return game_data

    def replace_in_game_data(self, game_data, value):
        """Replace content in the game data"""
        for key, content in value.items():
            if key in game_data:
                game_data[key] = content
        return game_data
```