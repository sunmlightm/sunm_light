# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestSinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parent_title = scrapy.Field()
    parent_url = scrapy.Field()
    son_title = scrapy.Field()
    son_url = scrapy.Field()
    parent_son_path = scrapy.Field()
    grandson_title = scrapy.Field()
    grandson_url = scrapy.Field()
    grandson_content = scrapy.Field()
    crawled = scrapy.Field()
    spider = scrapy.Field()
