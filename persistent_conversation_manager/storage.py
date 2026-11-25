import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)

HISTORY_FILE = DATA_DIR / "history.json"


def save_history(messages):
    with open(HISTORY_FILE,"w",encoding="utf-8") as file:
        json.dump(messages,file,indent=4)
    


def load_history():
    try:
        with open(HISTORY_FILE,"r",encoding="utf-8") as file:
                history_mess=json.load(file)
        if not isinstance(history_mess,list):
             raise ValueError("data is corrupted")
        return history_mess
    except FileNotFoundError:
            return []
    except json.JSONDecodeError:
           print("Conversation history is corrupted.")
           raise
         
                     


def add_message(role, content):
    role = role.strip().lower()

    if role not in ["user", "assistant", "system"]:
        raise ValueError("Enter a valid role")

    if not content.strip():
        raise ValueError("Enter valid content")

    messages = load_history()

    messages.append({
        "role": role,
        "content": content
    })

    save_history(messages)
    



def clear_history():
    save_history([])



def get_user_messages():
    messages=[]
    mess=load_history()
    for m in mess:
         if(m['role']=="user"):
              messages.append(m['content'])
    return messages


def get_recent_messages(n):
     if(n<0):
            print("enter Positive no")
            return []
     elif (n==0) :
            print("enter valid no")
            return []
     messages=load_history()
     return messages[-n:]


def count_messages():
    mess=load_history()
    return len(mess)