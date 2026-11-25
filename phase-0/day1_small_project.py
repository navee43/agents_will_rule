









messages=[]

def add_messages(role , content):
    if role not in ["system" , "user" ,"assistant"]:
        print("invalid role")
        return 
    
    if not content.strip():
        print("Message cannot be empty")
        return

    message={
        "role" :role,
        "content": content
    }
    messages.append(message)
print("message added successfully")


def display_history():
    if not messages:
        print("No messages available.")
        return

    for message in messages:
        print(f"{message['role']} : {message['content']}")


def get_user_messages():
   listing=[]
   for message in messages:
       if(message['role']=="user"):
            listing.append(message['content'])
   return listing



def get_recent_messages(n):
    if(n<0):
        print("enter Positive no")
        return
    elif (n==0) :
        print("enter valid no")
        return
    return messages[-n:]


def clear_history():
    messages.clear()
    print("message history cleard")


def count_messages():
    return len(messages)






while True:
    print("\n===== AI Conversation Manager =====")
    print("1. Add message")
    print("2. Display conversation history")
    print("3. Display user messages")
    print("4. Display recent messages")
    print("5. Count messages")
    print("6. Clear history")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        role = input("Enter role: ")
        content = input("Enter message: ")

        add_messages(role, content)

    elif choice == "2":
        display_history()


    elif choice == "3":
        print(get_user_messages())


    elif choice == "4":
        try:
             p = int(input("how many last msg you want "))
             print(get_recent_messages(p))
        except valueError:
            print("enter a valid no")

    elif choice == "5":
         print(count_messages())

    elif choice == "6":
         clear_history()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")

