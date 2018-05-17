# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Tencent.items import TencentItem

class Tencentposition2Spider(CrawlSpider):
    name = 'tencentPosition2'
    allowed_domains = ['hr.tencent.com']
    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(offset) + '#a']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        tr_lists = response.xpath('//tr[@class="odd"]|//tr[@class="even"]')
        for tr in tr_lists:
            item = TencentItem()
            position_name = tr.xpath('./td/a/text()').extract()[0]
            position_link = tr.xpath('./td/a/@href').extract()[0]
            item["position_name"] = position_name
            item["position_link"] = position_link
            yield item
