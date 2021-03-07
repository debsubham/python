import requests
from requests.api import request
from bs4 import BeautifulSoup
from random import choice


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



# print(next_btn)
# print(all_quotes)

def start_game():
    quote = choice(all_quotes)
    remaining_guesses = 4
    print(quote["quote"])
    print(quote["author"])
    guess = ""
    again =""

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
      guess = input(f"guess the author, remaining try{remaining_guesses}")
      remaining_guesses -= 1
      if remaining_guesses == 3:
        res = requests.get(f"{base_url}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        
        birth_date = soup.find(class_ = "author-born-date").get_text()
        birth_location = soup.find(class_ = "author-born-location").get_text()
        print("Here's a hints")
        print(f"born date: {birth_date} and location: {birth_location}")
      
    if remaining_guesses > 0:
      print("You Won the Game....")

    while again not in ("y","yes","n","no"):
        again = input("do you want to try again?")
    if again.lower() in ("yes","y"):
      print("Ok play Again")
      return start_game()
    else:
      print("Good Bye")

start_game()