# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader,Identity
from DownImg.items import DownimgItem


class DownimgSpider(scrapy.Spider):
    name = 'downimg'
    page = 1
    url = "http://www.meizitu.com/a/more_"
    start_urls = [url + str(page) + ".html"]

    def parse(self, response):
        links = response.xpath('//div[@class="pic"]/a/@href').extract()
        for link in links:
            yield  scrapy.Request(link,callback=self.downimage)

        if self.page<70:
            self.page+=1
            new_url = self.url + str(self.page) + ".html"
            yield  scrapy.Request(new_url, callback=self.parse)

    def downimage(self,response):
        item_loader = ItemLoader(item=DownimgItem(),response=response)
        item_loader.add_xpath("title",'//div[@class="metaRight"]/h2/a/text()')
        item_loader.add_value("url", response.url)
        item_loader.add_xpath("images", '//div[@id="picture"]/p/img/@src',Identity())
        return item_loader.load_item()