# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    newsid = scrapy.Field()
    nid = scrapy.Field()
    body = scrapy.Field()
    pass
