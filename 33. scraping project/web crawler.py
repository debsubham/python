import scrapy

class BookSpider(scrapy.Spider):
  name = "bookspider"
  start_urls = ["https://books.toscrap.com"]

  def parse(self, response):
      for article in response.css("article.product_pod"):
        yield {
          "price" : article.css(".price_color::text").extract_first(),
          "title" : article.css("h3 > a::attr(href)").extract_first()
        }
        next = response.css(".next > a::attr(href)").extract_first()
        if next : 
          yield response.follow(next, self.parse)