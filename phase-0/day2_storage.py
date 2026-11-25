import json



def save_history(messages):
    with open("history.json","w",encoding="utf-8") as file:
       json.dump(messages,file,indent=4)
     


def load_history():
  try:
     with open("history.json","r",encoding="utf-8") as file:
        read_file= json.load(file)
        return read_file
  except FileNotFoundError :
        return []
    


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



clear_history()

add_message("user", "What is an AI agent?")
add_message("assistant", "An AI agent can use tools.")
add_message("user", "What is tool calling?")

print(load_history())