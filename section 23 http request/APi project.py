import requests

url = "http://icanhazdadjoke.com/search"


print("Let me tell yoou a joke! Give me a topic:::")

answer = input("Answer ")

response = requests.get(url, headers={"Accept" : "application/json"}, params={"term" :answer, "limit" : 1})

total = response.json()["total_jokes"]

print(f"i have got {total} jokes about {answer}. Here's one::")
print(response.json()["results"][0]["joke"])


