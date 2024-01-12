import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawler.items import Content, Creator
from crawler import config


class PcolleSpider(CrawlSpider):
    # def __init__(self):
    #     self.DEBUG = config.DEBUG

    name = "pcolle"
    allowed_domains = ["www.pcolle.com"]
    start_urls = ["https://www.pcolle.com/product/result/"]

    if config.DEBUG:
        # Debug
        rules = (
            Rule(
                LinkExtractor(
                    restrict_css="div.wrap.search-list div div.main div.pagi ul li:nth-child(2)"
                ),
            ),
            Rule(
                LinkExtractor(
                    restrict_css="div.wrap.search-list div div.main div.top-main section ul li:nth-child(-n+4)"
                ),
                callback="parse_link",
            ),
        )
    else:
        # Prod
        rules = (
            Rule(
                LinkExtractor(restrict_css="div.wrap.search-list div div.main div.pagi ul li"),
            ),
            Rule(
                LinkExtractor(
                    restrict_css="div.wrap.search-list div div.main div.top-main section ul li"
                ),
                callback="parse_link",
            ),
        )

    def parse_link(self, response):
        if "product" in response.url:
            return self.parse_content(response)
        else:
            return self.parse_creator(response)

    def parse_content(self, response):
        content = Content()
        content["url"] = response.url
        content["name"] = response.css(
            "div.wrap.search-list > div > div.main > div.item-content > div > div.item-info.col-md-6.col-sm-6 > table > tbody tr:nth-child(4) td::text"
        ).extract_first()
        content["price"] = response.css(
            "div.wrap.search-list > div > div.main > div.item-content > div > div.item-info.col-md-6.col-sm-6 > table > tbody > tr:nth-child(1) > td > span::text"
        ).extract_first()
        content["creator"] = response.css(
            "div.wrap.search-list > div > div.main > div.item-content > div > div.item-info.col-md-6.col-sm-6 > table > tbody > tr:nth-child(2) > td > a::text"
        ).extract_first()
        return content

    def parse_creator(self, response):
        creator = Creator()
        creator["name"] = response.css("#bosyu_title > h1::text").extract_first()
        creator["name"] = creator["name"].split("さん")[0]
        creator["url"] = response.url
        return creator
