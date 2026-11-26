import os
import requests
from dotenv import load_dotenv

load_dotenv()


API_KEYS=os.getenv("GROQ_API_KEY")


if not API_KEYS:
    raise ValueError("api key not found")

url = "https://api.groq.com/openai/v1/chat/completions"

header={
    "Authorization" : f"Bearer {API_KEYS}",
    "Content-Type" : "Application/json"
}

payload = {
    "model": "openai/gpt-oss-120b",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": "Explain AI agents in simple words."
        }
    ],
    "temperature": 0.7,
    "max_completion_tokens": 1024
}



response = requests.post(
      url,
      headers=header,
      json=payload,
      timeout=60
      
)


response.raise_for_status()
data=response.json()

print(data["choices"][0]["message"]["content"]  )




print("Input tokens:", usage["prompt_tokens"])
print("Output tokens:", usage["completion_tokens"])
print("Total tokens:", usage["total_tokens"])