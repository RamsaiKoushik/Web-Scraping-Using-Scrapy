import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response, **kwargs):
        all_div_quotes = response.css("div.quote")[0]
        title = all_div_quotes.css("span.text::text").extract()
        author = all_div_quotes.css(".author::text").extract()
        tag = all_div_quotes.css(".tag::text").extract()
        # title = response.css('title').extract()
        yield {
            'title': title,
            'author': author,
            "tag": tag
               }
