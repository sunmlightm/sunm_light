# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader,Identity
from Meizitu.items import MeizituItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['meizitu.com']
    url = 'http://www.meizitu.com/a/more_'
    page = 1
    start_urls = [url + str(page) + '.html']

    def parse(self, response):
        links = response.xpath('//div[@class="pic"]/a/@href').extract()
        for link in links:
            yield scrapy.Request(link,callback=self.downimg)

        if self.page < 15:
            self.page += 1
            new_url = self.url + str(self.page) + ".html"
            yield scrapy.Request(new_url, callback=self.parse)


    def downimg(self,response):
        imgs = response.xpath('//div[@id="maincontent"]//p/img/@src').extract()
        titles = response.xpath('//div[@id="maincontent"]//p/img/@src').extract()
        for i in range(len(imgs)):
            item = MeizituItem()
            item['image'] = imgs[i]
            item['title'] = titles[i]
            yield item


