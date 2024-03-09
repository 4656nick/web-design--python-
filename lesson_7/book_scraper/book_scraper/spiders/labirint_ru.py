import scrapy


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
        name = response.css("div.prodtitle h1::text").re(r"(?<=: )(.+)")
        for detail in response.css("div.product-description"):
            author = detail.css("a.analytics-click-js::text").get()
            price = detail.css("span.buying-priceold-val-number::text").get()
            numberOfPages = detail.css("div.pages2::text").re(r"Страниц:\s*(\d+)")
            isbn = detail.css("div.isbn::text").re(r"ISBN:\s*(\d+-\d+-\d+-\d+-\d+)")
            publisher = detail.css("div.publisher a.analytics-click-js::text").get()
            if price is None:
                price = "Товара нет в наличии"
            return {
                "name": name[0],
                "author": author,
                "price": price,
                "numberOfPages": numberOfPages[0],
                "isbn": isbn[0],
                "publisher": publisher,
            }
