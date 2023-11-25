```python
import requests
from backend.integrations.gpt4_1106_previewAPI import sendChatCompletion

class AdaptiveResponseGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def generate_contextual_response(self, prompt, context):
        """
        Generate a response based on the given prompt and context using GPT-4-1106-preview API.
        :param prompt: The prompt to send to the AI.
        :param context: The context in which the prompt is being made.
        :return: The AI-generated response.
        """
        response = sendChatCompletion(prompt, context, self.headers)
        return response

    def adapt_response(self, ai_response, game_state):
        """
        Adapt the AI response to ensure it is contextually appropriate and maintains narrative consistency.
        :param ai_response: The initial response from the AI.
        :param game_state: The current state of the game to consider for the response.
        :return: The adapted response.
        """
        # Here we could implement additional logic to adapt the response based on the game state
        # For simplicity, we are returning the AI response directly
        return ai_response

# Example usage:
# adaptive_response_generator = AdaptiveResponseGenerator('your-api-key')
# prompt = "The goblin attacks you with a scimitar. What do you do?"
# context = {'previous_actions': ['You draw your sword', 'You approach the goblin cautiously']}
# ai_response = adaptive_response_generator.generate_contextual_response(prompt, context)
# adapted_response = adaptive_response_generator.adapt_response(ai_response, game_state={'combat': True})
```