```python
import re

class ContentFilter:
    def __init__(self):
        self.age_limit = 18
        self.explicit_words = ["explicit1", "explicit2", "explicit3"]  # Add explicit words here

    def set_age_limit(self, age):
        self.age_limit = age

    def add_explicit_word(self, word):
        self.explicit_words.append(word)

    def remove_explicit_word(self, word):
        if word in self.explicit_words:
            self.explicit_words.remove(word)

    def is_content_appropriate(self, text, player_age):
        if player_age < self.age_limit:
            return not any(word in text for word in self.explicit_words)
        return True

    def filter_content(self, text, player_age):
        if self.is_content_appropriate(text, player_age):
            return text
        else:
            return re.sub('|'.join(map(re.escape, self.explicit_words)), '[explicit]', text)
```