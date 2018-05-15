# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['hr.tencent.com']
    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(offset) + '#a']
    '''
        position_name = scrapy.Field()
        position_link = scrapy.Field()
        position_type = scrapy.Field()
        work_address = scrapy.Field()
        publish_time = scrapy.Field()
        position_number = scrapy.Field()
    '''

    def parse(self, response):
        tr_lists = response.xpath('//tr[@class="odd"]|//tr[@class="even"]')
        position_numbers = response.xpath('//tr[@class="f"]/td/div/span/text()').get()
        for tr in tr_lists:
            print("--" * 100)
            item = TencentItem()
            position_name = tr.xpath('./td/a/text()').extract()[0]
            position_link = tr.xpath('./td/a/@href').extract()[0]
            item["position_name"] = position_name
            item["position_link"] = position_link
            yield item

        if self.offset < int(position_numbers):
            self.offset += 10
        new_url = self.url + str(self.offset) + "#a"
        yield scrapy.Request(new_url,callback=self.parse)
