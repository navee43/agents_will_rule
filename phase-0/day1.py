modal_name="my_ai_modal"
max_iteration=5
temperature = 0.7
is_agent_active=True
response = None


print(modal_name)
print(type(modal_name))
print(response)


topic = "Ai Agents"
difficulty="hard"

prompt=f"explain {topic} in a {difficulty} way"
print(prompt)


tools=["calculate" , 4 , 5 , False ]
prompt =f"we have to {tools[0]} the sum of {tools[1]} and {tools[2]} and check if it is {tools[-1]}"

print(prompt)
tools.append("whether")
tools.remove("whether")
print(len(tools))

print(tools[1:])


message={
    "role":"dev",
    "content":"build ai agents"
}

print(message["role"])
print(message["content"])

message["role"]="user"
print(message)

# print(message["timestamp"])
print(message.get("timestamp","Not Available"))



messages = [
    {
        "role" : "System",
        "content":"You are a helpfull Ai Assistent"
    },
    {
        "role" : "User",
        "content" : "tell me about python"
    },
    {
        "role" : "ai Assistent",
        "content":"python is a programing language"
    }
]

print(messages[-2:])
print(messages[1]["content"])




""" Tuple and set"""

allowed_roles=("user" , "system" ,"assistant")



def add(a,b):
    return a+b


print(add(2,3))

def create_message(role,content):
    return {
        "role" : role,
        "content" :content
    }


print(create_message("user","what is python"))


def create_chat(Naveen , Rahul="hello"):
    return {
        "Naveen" : Naveen,
        "Rahul" : Rahul
    }



print(create_chat(Naveen="Hi",Rahul=" HI Naveen how you doin"))



messages=[]

def create_messages(Role , content):
    message = {
        "Role" : Role,
        "content" : content
    }
    messages.append(message)

create_messages(Role="user" , content="tell me about python")
create_messages("Ai Assistant" ,"python is a programming language")
create_messages("user","tell me more about python" )


print(messages[-2:])
for m in messages:
   if(m['Role']=="user"):
        print(f"{m['Role']} : {m['content']}")







"""another coding exercise"""

def get_user_messages(messages):
    listing=[]
    for m in messages :
        if(m['role']=="user"):
            listing.append(m['content'])

    return listing







messages = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "What is AI?"},
    {"role": "assistant", "content": "AI means artificial intelligence."},
    {"role": "user", "content": "What is RAG?"}
]

print(get_user_messages(messages))