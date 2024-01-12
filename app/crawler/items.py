# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Content(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    creator = scrapy.Field()
    genres = scrapy.Field()
    product_id = scrapy.Field()
    release_date = scrapy.Field()
    rating = scrapy.Field()
    views = scrapy.Field()
    image_urls = scrapy.Field()
    description = scrapy.Field()
    tags = scrapy.Field()
    file_name = scrapy.Field()
    file_size = scrapy.Field()


class Creator(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    profile = scrapy.Field()
    hp_url = scrapy.Field()


class Post(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()


class TutorialItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
