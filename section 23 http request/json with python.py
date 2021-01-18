###requests.get (url, headers={"Accept": "text/plain"})

import requests

url = "http://icanhazdadjoke.com/search"

response = requests.get(url, 
    headers = {"Accept" : "application/json"},
    params = {"term" : "cat", "limit" : 1})   ## eqivalent to ====> http://icanhazdadjoke.com/search?term=cat&limit=1

print(response.text) ## =====> it is string format not json, look like json
print(response.json()) ## ====> its actual JSON format
print(response.json()["status"])
print(response.json()["results"][0]["joke"])