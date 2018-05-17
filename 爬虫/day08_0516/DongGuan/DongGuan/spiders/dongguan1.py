# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from  DongGuan.items import DongguanItem


class Dongguan1Spider(CrawlSpider):
    name = 'dongguan1'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    rules = (
        Rule(LinkExtractor(allow=r'type=4')),
        Rule(LinkExtractor(allow=r'/question/\d+/\d+.shtml'), callback='parse_item', follow=False),
    )

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
