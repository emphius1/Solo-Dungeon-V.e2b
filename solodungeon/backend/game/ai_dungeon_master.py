```python
import openai
from .models import AIResponseModel
from .llm_integration import LLMInterface

class AIDungeonMaster:
    def __init__(self, api_key):
        self.api_key = api_key
        self.llm_interface = LLMInterface(api_key)

    def generate_narrative(self, prompt, context):
        """
        Generate a narrative based on the player's prompt and the current context of the game.
        """
        response = self.llm_interface.get_response(prompt, context)
        return response

    def process_player_action(self, action, context):
        """
        Process the player's action and return the AI Dungeon Master's response.
        """
        prompt = self.create_prompt_from_action(action, context)
        ai_response = self.generate_narrative(prompt, context)
        self.save_ai_response(ai_response)
        return ai_response

    def create_prompt_from_action(self, action, context):
        """
        Create a prompt for the LLM based on the player's action and the current game context.
        """
        # This function will need to be implemented based on the game's mechanics and how the
        # AI should interpret player actions.
        prompt = f"{context}\n\n{action}\n\nWhat happens next?"
        return prompt

    def save_ai_response(self, response):
        """
        Save the AI response to the database.
        """
        ai_response = AIResponseModel(response=response)
        ai_response.save()

    def adapt_to_player(self, player_profile):
        """
        Adapt the AI Dungeon Master's behavior based on the player's profile and past interactions.
        """
        # This function will need to be implemented to personalize the AI's behavior and responses.
        pass

# Example usage:
# ai_dungeon_master = AIDungeonMaster(api_key='your-api-key')
# context = "You are in a dark forest. A goblin stands before you."
# action = "I attack the goblin with my sword."
# response = ai_dungeon_master.process_player_action(action, context)
# print(response)
```