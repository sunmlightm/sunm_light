# -*- coding: utf-8 -*-
import scrapy
from Dongguan.items import DongguanItem

class DongguanSpider(scrapy.Spider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    def parse(self, response):
        links = response.xpath('//a[contains(@href,"/html/question/")]/@href').extract()
        for link in links:
            yield scrapy.Request(link,callback=self.dongparse)
        if self.offset<1000:
            self.offset+=30
            new_url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page=' + str(self.offset)
            yield scrapy.Request(new_url,callback=self.parse)


    def dongparse(self,response):
        item = DongguanItem()
        url = response.url
        text =response.xpath('//div[@class="pagecenter p3"]//strong/text()').get()
        title = text.split('  ')[0].split('：')[1]
        num = text.split('  ')[1].split(':')[1]
        item['num']= num
        item['title']= title
        item['url']= url
        yield item
