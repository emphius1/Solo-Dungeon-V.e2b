import openai
from django.conf import settings
from .models import AIResponseModel

class LLMIntegration:
    def __init__(self):
        self.openai_api_key = settings.OPENAI_API_KEY

    def generate_narrative(self, prompt, max_tokens=150):
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=max_tokens,
            api_key=self.openai_api_key
        )
        return response.choices[0].text.strip()

    def get_ai_response(self, player_input):
        narrative = self.generate_narrative(player_input)
        ai_response = AIResponseModel.objects.create(response=narrative)
        return ai_response

# Ensure to set the OPENAI_API_KEY in your settings or .env file
# Example usage:
# llm_integration = LLMIntegration()
# ai_response = llm_integration.get_ai_response("You enter a dimly lit tavern, what do you do?")
# print(ai_response.response)