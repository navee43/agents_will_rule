import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)

HISTORY_FILE = DATA_DIR / "history.json"

def save_history(messages):
  with open(HISTORY_FILE, "w", encoding="utf-8") as file:
       json.dump(messages,file,indent=4)
     


def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
          inside_data=json.load(file)
        if not isinstance(inside_data, list):
            raise ValueError("Conversation history must be a list")
        return inside_data

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Conversation history is corrupted.")
        raise
    


def add_message(role, content):
    listing = load_history()

    message = {
        "role": role,
        "content": content
    }

    listing.append(message)

    save_history(listing)


    


def clear_history():
    save_history([])





try:
    add_message("user", "What is an AI agent?")
    add_message("assistant", "An AI agent can use tools.")
    add_message("user", "What is tool calling?")

except json.JSONDecodeError:
    print("Cannot add message because history is corrupted.")

except ValueError as error:
    print(error)


print(load_history())