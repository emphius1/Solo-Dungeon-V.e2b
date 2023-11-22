# GPT-4-1106-preview API Interaction

This document outlines the interaction with the GPT-4-1106-preview API to support the dynamic AI interactions and narrative generation within our D&D application.

## Overview

The GPT-4-1106-preview API will be used to handle specific subtasks that are part of the core responsibilities of each Assistant. These subtasks include narrative generation, dynamic conversation handling, and decision-making support for the AI Dungeon Master.

## API Interaction Flow

1. **Initialization**: When the backend server starts, it initializes the API interaction module by loading the `apiEndpoints` configuration, which includes the `chatCompletionsEndpoint`.

2. **Request Preparation**: When a subtask requires the GPT-4-1106-preview API, the backend prepares a JSON payload with the necessary context and instructions. This payload is constructed by the `assistantSubtaskHelper.py` module.

3. **API Call**: The `sendChatCompletion()` function from `gpt4_1106_previewAPI.py` is invoked, which sends a POST request to the `chatCompletionsEndpoint` with the prepared payload.

4. **Response Handling**: Upon receiving the response, the backend parses the result and extracts the relevant information. If the response includes an action, the corresponding function within the game engine is called.

5. **Error Handling**: In case of an API error, the backend logs the incident and, depending on the severity, either retries the request or defaults to a predefined behavior.

6. **Rate Limiting and Quotas**: The backend monitors the number of requests to avoid exceeding the API's rate limits and quotas, implementing a retry mechanism with exponential backoff if necessary.

## Sample Code for API Interaction

```python
import requests
from backend.helpers.assistantSubtaskHelper import prepare_payload
from backend.integrations.gpt4_1106_previewAPI import sendChatCompletion

def handle_narrative_generation(context):
    payload = prepare_payload(context, task="generate_narrative")
    response = sendChatCompletion(payload)
    return response

def sendChatCompletion(payload):
    try:
        response = requests.post(
            apiEndpoints['chatCompletionsEndpoint'],
            headers={'Authorization': f'Bearer {API_KEY}'},
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        # Log error and handle accordingly
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        # Log error and handle accordingly
        print(f"An error occurred: {err}")

# Example usage
context = {
    "previous_messages": [
        {"role": "system", "content": "You are in a dark forest."},
        {"role": "user", "content": "I look around for any signs of danger."}
    ]
}
narrative_response = handle_narrative_generation(context)
print(narrative_response)
```

## Security Considerations

- API keys and sensitive data are stored securely and not hard-coded into the application.
- Requests to the API are made over HTTPS to ensure data encryption in transit.
- Access to the API interaction module is restricted to authorized backend services only.

## Conclusion

The integration with the GPT-4-1106-preview API is a critical component of our application, enabling rich and dynamic AI-driven interactions. This document will be updated as the implementation evolves and as we iterate based on user feedback and testing.