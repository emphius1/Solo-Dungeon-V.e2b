```python
import openai

class GPT4_0613:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = "gpt-4-0613"
        openai.api_key = self.api_key

    def generate_response(self, prompt, max_tokens=100):
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

    def instruct(self, instruction, max_tokens=100):
        prompt = f"{instruction}\n\n"
        return self.generate_response(prompt, max_tokens)

    def push_to_github(self, file_path, commit_message):
        # This function assumes that you have set up GitHub CLI and the repository on your local machine.
        # Please replace 'main' with your default branch if it's not 'main'.
        import os
        os.system(f"git add {file_path}")
        os.system(f'git commit -m "{commit_message}"')
        os.system("git push origin main")
```
