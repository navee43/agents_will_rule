import requests

url = "https://api.github.com/users/navee43"

response = requests.get(url)

data = response.json()

print(data['name'])
print(data["login"])
print(data["name"])
print(data["followers"])
print(data["public_repos"])



url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Learning AI Agents",
    "body": "My first POST request using Python.",
    "userId": 1
}

response = requests.post(
    url,
    json=payload,
    timeout=10
)

response.raise_for_status()

print(response.status_code)
print(response.json())
