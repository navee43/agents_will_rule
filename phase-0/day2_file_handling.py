# file = open("history.txt" ,"w", encoding="utf-8")

# file.write("user : what is an ai agent")

# file.close()

# file = open("history.txt","r",encoding="utf-8")
# content=file.read()

# file.close()
# print(content)
file=open("history.txt","a",encoding="utf-8")
file.write("\nassistant : An ai agent can use tools to complete task")
file.close()

file = open("history.txt","r",encoding="utf-8")
for line in file:
    print(line.strip())

file.close()

file = open("history.txt","w",encoding="utf-8")
file.write("user : i am naveen")

file.close()

file = open("history.txt","a",encoding="utf-8")
file.write("\nai :Hi naveen")

file.close()

file = open("history.txt","r",encoding="utf-8")
content = file.readlines()
file.close()
print(content)

# for line in file:
#     print(line.strip())

# file.close()


