import requests
import json
import os


OPENAPI_API_KEY = os.environ.get('OPENAPI_API_KEY', 'development_key')
OPENAPI_MAX_TOKENS = os.environ.get('OPENAPI_MAX_TOKENS', '512')
OPENAPI_MODEL = os.environ.get('OPENAPI_MODEL', 'gpt-3.5-turbo')
OPENAPI_USER = os.environ.get('OPENAPI_USER', 'development_user')


class OpenAI:
    url = 'https://api.openai.com/v1'
    url_chat_completion = 'https://api.openai.com/v1/chat/completions'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {OPENAPI_API_KEY}'}

    def get_chat_completions(self, data: str) -> str:
        response = requests.post(
            url=self.url_chat_completion,
            headers=self.headers,
            data=json.dumps({
                "messages": [{"role": "user", "content": data}],
                "model": OPENAPI_MODEL,
                'max_tokens': OPENAPI_MAX_TOKENS,
                'user': OPENAPI_USER
            }))

        if response.status_code != 200:
            raise Exception('Error during OpenAI Completion')

        return response.json()['choices'][0]['message']['content']
