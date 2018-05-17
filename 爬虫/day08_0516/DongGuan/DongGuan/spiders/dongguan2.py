# -*- coding: utf-8 -*-
import scrapy
from  DongGuan.items import DongguanItem


class Dongguan2Spider(scrapy.Spider):
    offset=0
    url='http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    name = 'dongguan2'
    allowed_domains = ['wz.sun0769.com']
    start_urls = [url]


    def parse(self, response):
        links = response.xpath('//a[contains(@href,"/html/question/")]/@href').extract()
        for link in links:
            yield  scrapy.Request(link,callback=self.parse_item)

        if self.offset < 1000:
            self.offset += 30
            new_url = self.url + str(self.offset)
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_item(self, response):
        item = DongguanItem()
        url = response.url
        text = response.xpath('//div[@class="pagecenter p3"]//strong/text()').get()
        title = text.split('  ')[0].split('：')[1]
        number = text.split('  ')[1].split(':')[1]
        content = response.xpath('//div[@class="c1 text14_2"]/text()|//div[@class="contentext"]/text()').extract()
        content = ''.join(content)

        item['url']=url
        item['title']=title
        item['number']=number
        item['content']=content
        yield item