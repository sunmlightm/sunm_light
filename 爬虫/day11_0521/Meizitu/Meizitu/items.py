# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    # 帖子对应的多张图片路径
    image = scrapy.Field()
    # 帖子的链接
    url = scrapy.Field()
    # 图片保存的多个路径
    image_paths = scrapy.Field()
