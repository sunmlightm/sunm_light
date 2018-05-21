# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os
from test_sina.items import TestSinaItem


class Sina2Spider(CrawlSpider):
    name = 'sina2'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']
    # v<a href="http://news.sina.com.cn/china/">国内</a>
    # < a
    # href = "http://news.sina.com.cn/c/gat/2018-05-18/doc-ihaturfs2883813.shtml"


    rules = (
        # Rule(LinkExtractor(allow=r'.*.sina.com.cn/.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.*.sina.com.cn/.*shtml'), callback='detail_parse', follow=True),

    )


    # def parse(self, response):
    #
    #     parent_titles = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()
    #     parent_urls = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()
    #     son_titles = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()
    #     son_urls = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()
    #
    #     self.items = []
    #     for i in range(len(parent_titles)):
    #         parent_title = "./Data/" + parent_titles[i]
    #         parent_url = parent_urls[i]
    #         for j in range(len(son_titles)):
    #             son_title = son_titles[j]
    #             son_url = son_urls[j]
    #
    #             if son_url.startswith(parent_url):
    #                 parent_son_path = parent_title + "/" + son_title
    #                 if not os.path.exists(parent_son_path):
    #                     os.makedirs(parent_son_path)
    #
    #                 item = TestSinaItem()
    #                 item["parent_title"] = parent_title
    #                 item["parent_url"] = parent_url
    #                 item["son_title"] = son_title
    #                 item["son_url"] = son_url
    #                 item["parent_son_path"] = parent_son_path
    #                 self.items.append(item)

    def parse_item(self, response):
        print('2'*200)
        meta_item = self.meta["meta_item"]
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



    def detail_parse(self, response):
        print('3'*200)
        item = response.meta["meta_item2"]
        grandson_title = response.xpath('//h1[@id="artibodyTitle"]/text()|//h1[@class="main-title"]/text()').extract()
        grandson_title = ''.join(grandson_title)
        grandson_content = response.xpath('//div[@id="article"]/p[position()>1]/text()|//div[@id="artibody"]/p/text()').extract()
        grandson_content = "".join(grandson_content)
        item["grandson_title"] = grandson_title
        item["grandson_content"] = grandson_content
        print(item)
