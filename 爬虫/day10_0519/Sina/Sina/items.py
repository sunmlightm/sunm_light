# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
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


#     def parse(self, response):
#         parent_titles = response.xpath('//div[@id="tab01"]//h3/a/text()').extract()
#         parent_urls = response.xpath('//div[@id="tab01"]//h3/a/@href').extract()
#         son_titles = response.xpath('//div[@id="tab01"]//ul/li/a/text()').extract()
#         son_urls = response.xpath('//div[@id="tab01"]//ul/li/a/@href').extract()
#
#         items = []
#         for i in range(len(parent_titles)):
#             parent_title = "./Data/" + parent_titles[i]
#             parent_url = parent_urls[i]
#             for j in range(len(son_titles)):
#                 son_title = son_titles[j]
#                 son_url = son_urls[j]
#
#                 if son_url.startswith(parent_url):
#                     parent_son_path = parent_title + "/" + son_title
#                     if not os.path.exists(parent_son_path):
#                         os.makedirs(parent_son_path)
#
#                     item = SinaItem()
#                     item["parent_title"] = parent_title
#                     item["parent_url"] = parent_url
#                     item["son_title"] = son_title
#                     item["son_url"] = son_url
#                     item["parent_son_path"] = parent_son_path
#                     items.append(item)
#
#         for item in items:
#             son_url = item["son_url"]
#             yield scrapy.Request(son_url, callback=self.seconde_parse, meta={"meta_item": item})


#     def parse(self, response):
#         print('1' * 200)
#
#         parent_titles = response.xpath('//div[@id="tab01"]//h3/a/text()').extract()
#         parent_urls = response.xpath('//div[@id="tab01"]//h3/a/@href').extract()
#         son_titles = response.xpath('//div[@id="tab01"]//ul/li/a/text()').extract()
#         son_urls = response.xpath('//div[@id="tab01"]//ul/li/a/@href').extract()
#         items = []
#         for i in range(len(parent_titles)):
#             parent_title = './Data/' + parent_titles[i]
#             parent_url = parent_urls[i]
#
#             for j in range(len(son_titles)):
#                 son_title = son_titles[j]
#                 son_url = son_urls[j]
#
#                 if son_url.startswith(parent_url):
#                     item = SinaItem()
#
#                     parent_son_path = parent_title + "/" + son_title
#
#                     # if not os.path.exists(parent_son_path):
#                     #     os.makedirs(parent_son_path)
#
#                     item["parent_title"] = parent_title
#                     item["parent_url"] = parent_url
#                     item["son_title"] = son_title
#                     item["son_url"] = son_url
#                     item["parent_son_path"] = parent_son_path
#                     items.append(item)
#
#         for item in items:
#             yield scrapy.Request(son_url,callback=self.seconde_parse,meta={'meta_item':item})