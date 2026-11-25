


def save_message(role, content):
    if role not in ["user" , "Assistant" , "system"]:
       print("role not valid")
       return
    if not content.strip():
        print("enter valid content")
        return
    
    with open("history.txt","a",encoding="utf-8") as file:
        file.write(f"{role} : {content}\n")
     
   


def read_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return "No conversation history available."


def clear_history():
    with open("history.txt","w",encoding="utf-8") as file:
       pass
  




# clear_history()

# save_message("user", "What is RAG?")
# save_message("assistant", "RAG retrieves relevant information.")
# save_message("user", "How does it work?")

# print(read_history())
