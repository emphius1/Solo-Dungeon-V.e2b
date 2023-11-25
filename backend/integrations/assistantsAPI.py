import requests
import json
from backend.helpers.assistantSubtaskHelper import fetchAssistantAction, sendChatCompletion

# Constants for API endpoints
ASSISTANTS_ENDPOINT = "https://api.openai.com/v1/assistants"
CHAT_COMPLETIONS_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Your OpenAI API key
OPENAI_API_KEY = "your-api-key"

class AssistantsAPI:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

    def create_assistant(self, model, assistant_task):
        """
        Create an assistant for a specific task.
        :param model: The model to be used by the assistant.
        :param assistant_task: The task the assistant will perform.
        :return: Assistant ID or error message.
        """
        payload = {
            "model": model,
            "task": assistant_task
        }
        response = requests.post(ASSISTANTS_ENDPOINT, headers=self.headers, json=payload)
        if response.status_code == 201:
            return response.json().get("id")
        else:
            return f"Error: {response.json().get('error', 'Unknown error')}"

    def call_assistant_action(self, assistant_id, action, parameters):
        """
        Call an action for the assistant to perform.
        :param assistant_id: The ID of the assistant.
        :param action: The action to be performed.
        :param parameters: Parameters for the action.
        :return: Result of the action or error message.
        """
        payload = {
            "assistant_id": assistant_id,
            "action": action,
            "parameters": parameters
        }
        response = requests.post(f"{ASSISTANTS_ENDPOINT}/{assistant_id}/actions", headers=self.headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.json().get('error', 'Unknown error')}"

    def get_assistant_response(self, assistant_id, prompt):
        """
        Get a response from the assistant based on a prompt.
        :param assistant_id: The ID of the assistant.
        :param prompt: The prompt to send to the assistant.
        :return: Assistant's response or error message.
        """
        payload = {
            "assistant_id": assistant_id,
            "prompt": prompt
        }
        response = requests.post(f"{ASSISTANTS_ENDPOINT}/{assistant_id}/messages", headers=self.headers, json=payload)
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", "")
        else:
            return f"Error: {response.json().get('error', 'Unknown error')}"

    def perform_subtask_with_gpt4_1106_preview(self, subtask_instruction):
        """
        Perform a subtask using the GPT-4-1106-preview API.
        :param subtask_instruction: The instruction for the subtask.
        :return: Result of the subtask or error message.
        """
        payload = {
            "model": "gpt-4-1106-preview",
            "messages": [{"role": "system", "content": subtask_instruction}]
        }
        response = requests.post(CHAT_COMPLETIONS_ENDPOINT, headers=self.headers, json=payload)
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", "")
        else:
            return f"Error: {response.json().get('error', 'Unknown error')}"

# Example usage
if __name__ == "__main__":
    assistants_api = AssistantsAPI()
    assistant_id = assistants_api.create_assistant("davinci", "Dungeon Master")
    if isinstance(assistant_id, str) and not assistant_id.startswith("Error"):
        action_result = assistants_api.call_assistant_action(assistant_id, fetchAssistantAction("Dungeon Master"), {})
        print(action_result)
        assistant_response = assistants_api.get_assistant_response(assistant_id, "Start the game")
        print(assistant_response)
        subtask_result = assistants_api.perform_subtask_with_gpt4_1106_preview("Describe a dark forest scene.")
        print(subtask_result)
    else:
        print(assistant_id)