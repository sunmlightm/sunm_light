# -*- coding: utf-8 -*-
import scrapy,os
from test_sina.items import TestSinaItem
from scrapy_redis.spiders import RedisCrawlSpider

class Sina1Spider(RedisCrawlSpider):
    name = 'sina1'
    redis_key = 'sinaspider:start_urls'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']


    #     parent_title = scrapy.Field()
    #     parent_url = scrapy.Field()
    #     son_title = scrapy.Field()
    #     son_url = scrapy.Field()
    #     parent_son_path = scrapy.Field()
    #     grandson_title = scrapy.Field()
    #     grandson_url = scrapy.Field()
    #     grandson_content = scrapy.Field()

    def parse(self, response):
        parent_titles = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()
        parent_urls = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()
        son_titles = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()
        son_urls = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()

        items = []
        for i in range(len(parent_titles)):
            parent_title = "./Data/" + parent_titles[i]
            parent_url = parent_urls[i]
            for j in range(len(son_titles)):
                son_title = son_titles[j]
                son_url = son_urls[j]

                if son_url.startswith(parent_url):
                    parent_son_path = parent_title + "/" + son_title
                    if not os.path.exists(parent_son_path):
                        os.makedirs(parent_son_path)

                    item = TestSinaItem()
                    item["parent_title"] = parent_title
                    item["parent_url"] = parent_url
                    item["son_title"] = son_title
                    item["son_url"] = son_url
                    item["parent_son_path"] = parent_son_path
                    items.append(item)

        for item in items:
            son_url = item["son_url"]
            yield scrapy.Request(son_url, callback=self.seconde_parse, meta={"meta_item": item})

    def seconde_parse(self,response):
        meta_item = response.meta["meta_item"]
        url_list = response.xpath('//a/@href').extract()
        items = []
        for url in url_list:
            parent_url = meta_item["parent_url"]
            if url.startswith(parent_url) and url.endswith(".shtml"):
                grandson_url = url
                item = TestSinaItem()
                item["parent_title"] = meta_item["parent_title"]
                item["parent_url"] = meta_item["parent_url"]
                item["son_title"] = meta_item["son_title"]
                item["son_url"] = meta_item["son_url"]
                item["parent_son_path"] = meta_item["parent_son_path"]
                item["grandson_url"] = grandson_url
                items.append(item)
        for item in items:
            grandson_url = item["grandson_url"]
            yield scrapy.Request(grandson_url, callback=self.detail_parse, meta={"meta_item2": item})


    def detail_parse(self, response):
        item = response.meta["meta_item2"]
        grandson_title = response.xpath('//h1[@id="artibodyTitle"]/text()|//h1[@class="main-title"]/text()').extract()
        grandson_title = ''.join(grandson_title)
        grandson_content = response.xpath('//div[@id="article"]/p[position()>1]/text()|//div[@id="artibody"]/p/text()').extract()
        grandson_content = "".join(grandson_content)
        item["grandson_title"] = grandson_title
        item["grandson_content"] = grandson_content
        yield item