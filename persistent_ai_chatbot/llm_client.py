import requests

from auth import build_headers



URL = "https://api.groq.com/openai/v1/chat/completions"



def build_payload(messages, model, temperature):

    system_messages = [
           {
            "role": "system",
            "content": "You are a helpful AI assistant. Give short and clear answers."
           }
                      ]

    # Combine system_messages with messages
    messages =system_messages+messages

    # Construct payload dictionary

    payload={
               "model":model,
               "messages": messages,
                "temperature": temperature,
                "max_completion_tokens":100
        
                }

    # Return payload

    return payload  


def call_llm(messages, config):

    headers = build_headers(config["API_KEY"])

    payload = build_payload(
        messages,
        config["MODEL_NAME"],
        config["TEMPERATURE"]
    )

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        raise RuntimeError("LLM request timed out.")

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Could not connect to Groq.")

    except requests.exceptions.HTTPError as error:
        raise RuntimeError(f"Groq API error: {error}")

    except requests.exceptions.JSONDecodeError:
        raise RuntimeError("Groq returned invalid JSON.")

    except requests.exceptions.RequestException:
        raise RuntimeError("LLM request failed.")

  

    


def extract_response(data):

    content = data["choices"][0]["message"]["content"]

    usage = data.get("usage", {})

    return {
        "answer": content,
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "total_tokens": usage.get("total_tokens"),
        "model": data["model"]
    }
   

    