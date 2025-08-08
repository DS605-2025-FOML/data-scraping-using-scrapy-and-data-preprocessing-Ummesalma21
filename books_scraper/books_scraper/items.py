# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    stock_availability = scrapy.Field()
    thumbnail = scrapy.Field()
    rating = scrapy.Field()
