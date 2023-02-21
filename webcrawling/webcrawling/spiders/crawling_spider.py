from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class crawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domain = ["toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/page/10/",
                  "http://quotes.toscrape.com/page/9/",
                  "http://quotes.toscrape.com/page/8/",
                  "http://quotes.toscrape.com/page/7/",
                  "http://quotes.toscrape.com/page/6/"
                  "http://quotes.toscrape.com/page/5/",
                  "http://quotes.toscrape.com/page/4/",
                  "http://quotes.toscrape.com/page/3/",
                  "http://quotes.toscrape.com/page/2/",
                  "http://quotes.toscrape.com/page/1/",
                  ]

    rules = (
        Rule(LinkExtractor(allow="tag"), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {
            "quote": response.css(".quote span::text").get(),
            "author": response.css(".author::text").get(),
            "tags": response.css(".keywords::attr(content)").get()
        }
