import json

# message = {
#     "role": "user",
#     "content": "Hello",
#     "active": True
# }

# result = json.dumps(message, indent=4)



# print(result)


# json_message = '{"role": "user", "content": "Hello"}'

# message = json.loads(json_message)

# print(message)
# print(type(message))
# print(message["content"])



# messages = [
#     {"role": "user", "content": "Hello"},
#     {"role": "assistant", "content": "Hi"}
# ]


# message = {"role": "user"}

# result = json.dumps(message)

# print(result["role"])


# data = '{"role": "user",}'

# result = json.loads(data)







def serialize_messages(messages):
       json_mess = json.dumps(messages ,indent=4)
       return json_mess
    


def deserialize_messages(json_data):
    string_mess = json.loads(json_data)
    return string_mess


def get_user_messages(json_data):
    string_mess=json.loads(json_data)
    for message in string_mess:
         if(message['role']=="user"):
              return message['content']







messages = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "What is AI?"},
    {"role": "assistant", "content": "AI means artificial intelligence."},
    {"role": "user", "content": "What is RAG?"}
]

json_data = serialize_messages(messages)

print(json_data)
print(type(json_data))

restored_messages = deserialize_messages(json_data)

print(restored_messages)
print(type(restored_messages))

print(get_user_messages(json_data))

print(messages == restored_messages)