```python
import json
import difflib

class SpellLookup:
    def __init__(self):
        with open('data/spells.json', 'r') as f:
            self.spells = json.load(f)

    def get_spell(self, spell_name):
        """Return the spell details if it exists, else return None."""
        return self.spells.get(spell_name.lower(), None)

    def get_close_matches(self, spell_name):
        """Return a list of spell names that closely match the input."""
        return difflib.get_close_matches(spell_name.lower(), self.spells.keys())

    def correct_spell_name(self, spell_name):
        """Correct the spell name if it is misspelled."""
        close_matches = self.get_close_matches(spell_name)
        if close_matches:
            return close_matches[0]
        return None
```