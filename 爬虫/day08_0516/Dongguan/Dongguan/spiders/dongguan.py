# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dongguan.items import DongguanItem
import json

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    # <a href="http://wz.sun0769.com/index.php/question/questionType?type=4&amp;page=">1</a>

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page')),
        Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), callback='parse_item', follow=False),
    )

    #     title = scrapy.Field()
    #     number = scrapy.Field()
    #     content = scrapy.Field()
    #     url = scrapy.Field()

    def parse_item(self, response):
        item = DongguanItem()
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        url = response.url
        text = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        title = text.split('  ')[0].split('：')[1]
        number = text.split('  ')[1].split(':')[1]
        content=response.xpath('//div[@class="c1 text14_2"]/text()|//div[@class="contentext"]/text()').extract()
        content = ''.join(content)
        item['title']=title
        item['number']=number
        item['content']=content
        item['url']=url
        yield item
