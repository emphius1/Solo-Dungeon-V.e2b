import requests
import json
from backend.integrations.gpt4_1106_previewAPI import sendChatCompletion
from backend.helpers.assistantSubtaskHelper import fetchAssistantAction

class ConversationalAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def generate_response(self, prompt, context):
        """
        Generate a response from the AI Dungeon Master based on the prompt and context provided.
        """
        response = sendChatCompletion(prompt, context)
        return response

    def handle_player_input(self, player_input, context):
        """
        Handle player input, generate appropriate responses, and manage the conversation state.
        """
        # Fetch the action from the Assistant based on the player's input
        action = fetchAssistantAction(player_input)

        # Generate a response from the AI Dungeon Master
        ai_response = self.generate_response(action, context)

        # Return the AI Dungeon Master's response
        return ai_response

    def engage_in_conversation(self, player_id, context):
        """
        Engage in a conversation with the player, providing adaptive responses and maintaining narrative consistency.
        """
        # Placeholder for conversation loop, which would be more complex in a real implementation
        while True:
            player_input = input("Enter your message to the AI Dungeon Master: ")
            if player_input.lower() == 'quit':
                break
            response = self.handle_player_input(player_input, context)
            print(response)

# Example usage:
# api_key = 'your-api-key-here'
# conversational_ai = ConversationalAI(api_key)
# context = {'previous_dialogue': []}  # This would be the actual context from the game
# conversational_ai.engage_in_conversation(player_id='player123', context=context)