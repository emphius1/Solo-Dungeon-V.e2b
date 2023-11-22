from django.test import TestCase
from game.llm_integration import getAIResponse
from game.models import AIResponseModel

class LLMIntegrationTest(TestCase):
    def setUp(self):
        # Setup initial data or mocks if necessary
        pass

    def test_get_ai_response(self):
        # Simulate player input
        player_input = "I approach the mysterious figure in the corner of the tavern."

        # Call the LLM integration function to get a response
        ai_response = getAIResponse(player_input)

        # Check if the response is not empty
        self.assertNotEqual(ai_response, "", "The AI response should not be empty.")

        # Check if the response is an instance of the expected schema
        self.assertIsInstance(ai_response, AIResponseModel, "The AI response should be an instance of AIResponseModel.")

    def test_ai_response_adapts_to_player(self):
        # Simulate player input and context
        player_input = "I draw my sword and prepare for battle."
        context = {
            'previous_actions': [
                "The goblin charges at you with a screeching yell.",
                "I ready my shield and brace for impact."
            ]
        }

        # Call the LLM integration function to get a response
        ai_response = getAIResponse(player_input, context)

        # Check if the response is contextually relevant
        self.assertIn("battle", ai_response.text, "The AI response should be relevant to the context of battle.")

    def test_ai_response_continuity(self):
        # Simulate a sequence of player inputs
        inputs = [
            "I ask the shopkeeper about any rumors.",
            "Do you have any special items for sale?",
            "I'll take the enchanted amulet, how much?"
        ]

        # Simulate a continuous conversation with the AI
        conversation_context = []
        for player_input in inputs:
            ai_response = getAIResponse(player_input, {'previous_actions': conversation_context})
            conversation_context.append(ai_response.text)

        # Check if the conversation flows logically
        self.assertTrue(all(response for response in conversation_context), "All AI responses in the conversation should be logical and non-empty.")