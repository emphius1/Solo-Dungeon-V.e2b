```python
import json
from gpt.model_integration import GPT4_0613

class ContextManager:
    def __init__(self):
        self.model = GPT4_0613()
        self.context = ""

    def update_context(self, new_context):
        self.context += new_context

    def reset_context(self):
        self.context = ""

    def get_context(self):
        return self.context

    def generate_response(self, prompt):
        full_prompt = self.context + prompt
        response = self.model.generate_response(full_prompt)
        self.update_context(response)
        return response

    def save_context(self):
        with open('context.json', 'w') as f:
            json.dump(self.context, f)

    def load_context(self):
        with open('context.json', 'r') as f:
            self.context = json.load(f)
```