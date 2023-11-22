import requests
import json
from .apiEndpoints import chatCompletionsEndpoint

class GPT4_1106_previewAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_prompt(self, prompt, session_id=None):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'gpt-4-1106-preview',
            'messages': [
                {
                    'role': 'system',
                    'content': 'You are a helpful assistant.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        }
        if session_id:
            data['session_id'] = session_id

        response = requests.post(chatCompletionsEndpoint, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error in GPT-4-1106-preview API call: {response.status_code} - {response.text}")

    def get_adaptive_response(self, prompt, context, session_id=None):
        full_prompt = f"{context}\n\n{prompt}"
        return self.send_prompt(full_prompt, session_id=session_id)

# Example usage:
# gpt_api = GPT4_1106_previewAPI('your-api-key')
# response = gpt_api.get_adaptive_response('How should I handle an orc encounter?', 'The party is low on health and without spells.')
# print(response)