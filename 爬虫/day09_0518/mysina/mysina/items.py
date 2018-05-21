# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MysinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parent_title = scrapy.Field()
    parent_urls = scrapy.Field()

    # 小类的标题和url
    sub_title = scrapy.Field()
    sub_urls = scrapy.Field()

    # 小类的标题下链接对应的要存储本地路径
    sub_file_name = scrapy.Field()

    # 小类的标题下对应的链接
    son_urls = scrapy.Field()

    # 文章的标题和内容
    head = scrapy.Field()
    content = scrapy.Field()
