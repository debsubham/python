import requests
from requests.api import request
from bs4 import BeautifulSoup

all_quotes = []

# res = requests.get("https://quotes.toscrape.com")
# print(res)
# soup = BeautifulSoup(res.text)
# quotes = soup.find_all(class_ = "quote")
# print(quotes)


base_url = "https://quotes.toscrape.com"
url = "/page/1"

while url:
    res = requests.get(f"{base_url}{url}")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_ = "quote")
    
    for quote in quotes:
      
      # text = quote.find(class_ = "text").get_text()
      # print(text)

      all_quotes.append({
        "quote" : quote.find(class_ = "text").get_text(),
        "author" : quote.find(class_ = "author").get_text(),
        "bio-link" :  quote.find("a")["href"]
      })
    # print(all_quotes)
    next_btn = soup.find(class_ = "next")
    url = next_btn.find("a")["href"] if next_btn else None



print(next_btn)
print(all_quotes)