##www.rithmschool.com/blog

import requests 
from bs4 import BeautifulSoup
import csv
from csv import writer
response = requests.get("https://www.rithmschool.com/blog")


mainfile= response.text
files = open("scraping_data.html", "w+")
files.write(mainfile)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
# print(articles)

# for article in articles:
#   # print(article.find("a"))
#   a_tags = article.find("a")
#   title =a_tags.get_text()
#   url = a_tags["href"]
#   # print(article.find("a").attrs) ## or article.find("a").attrs["href"] or article.find("a")["href"]
#   dates = article.find("time")
#   date = article.find("time")["datetime"]
#   # print(dates["datetime"])


with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link","date"])
    for article in articles:
        # print(article.find("a"))
        a_tags = article.find("a")
        title =a_tags.get_text()
        url = a_tags["href"]
        # print(article.find("a").attrs) ## or article.find("a").attrs["href"] or       article.find("a")["href"]
        dates = article.find("time")
        date = article.find("time")["datetime"]
        # print(dates["datetime"])
        csv_writer.writerow([title,url,date])