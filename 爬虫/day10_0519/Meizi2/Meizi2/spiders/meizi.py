# -*- coding: utf-8 -*-
import scrapy
from Meizi2.items import Meizi2Item
from scrapy.contrib.loader import ItemLoader


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['meizitu.com']
    offset = 1
    url = 'http://www.meizitu.com/a/more_'
    start_urls = [url + str(offset)+ '.html']

    def parse(self, response):
        pass
    item = ItemLoader()
