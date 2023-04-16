import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response, **kwargs):
        title = response.css('title').extract()
        yield {'title': title}
