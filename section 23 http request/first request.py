########## python -m pip install requests

import requests

aaaaa = requests.get("https://www.google.com")

print(aaaaa.ok)
print(aaaaa.headers)
print(aaaaa.text)
