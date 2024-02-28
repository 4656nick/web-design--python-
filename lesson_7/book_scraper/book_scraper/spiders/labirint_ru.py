import scrapy


class BookSpecs():
    name: str
    authors: str
    price: int
    isbn: str
    publisher: str
    numberOfPages: int
    year: int


class QuotesSpider(scrapy.Spider):
    name = "Book_Labirint"

    def start_requests(self):
        urls = ["https://www.labirint.ru/books/571931/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f"labirint-{page}.html"
        # Path(filename).write_bytes(response.body)
        for detail in response.css("div.product-description"):
            author = detail.css("a.analytics-click-js::text").get()
            price = detail.css("span.buying-priceold-val-number::text").get()
            numberOfPages = detail.css(
                "div.pages2::text").get()  # требуется регулярка чтобы страницы вытащить из текста
            isbn = detail.css("div.isbn::text").get()  # требуется регулярка чтобы вытащить номер ISBN
            publisher = detail.css("div.publisher a.analytics-click-js::text").get()
            print(dict(
                author=author,
                price=price,
                numberOfPages=numberOfPages,
                isbn=isbn,
                publisher=publisher
            ))
