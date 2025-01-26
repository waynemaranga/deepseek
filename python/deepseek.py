# DeepSeek API Docs: https://api-docs.deepseek.com/
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()
DEEPSEEK_API_KEY = getenv("DEEPSEEK_API_KEY")

# RAW version: using http requests to the DeepSeek API
def make_request(
        prompt: str,
        model="deepseek-chat", # Models and Pricing: https://api-docs.deepseek.com/quick_start/pricing
        system_role="You are a helpful assistant.",
        stream=False,
        ):
    
    base_url = "https://api.deepseek.com/chat/completions"
    headers = { "Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}" }
    data = {
        "model": model,
        "messages": [
            { "role": "system", "content": system_role },
            { "role": "user", "content": prompt }
        ],
        "stream": stream
    }

    response = requests.post(base_url, headers=headers, json=data)
    return response.text


if __name__ == "__main__":
    # print(DEEPSEEK_API_KEY)
    print(make_request(prompt="Hello, how are you?"))
    
    print("\n🐬")
