# -*- coding: utf-8 -*-
import scrapy
from MyScrapy.items import MyscrapyItem

class AtguiguSpider(scrapy.Spider):
    name = 'atguigu'
    allowed_domains = ['atguigu.com']
    start_urls = ['http://www.atguigu.com/teacher.shtml']

    def parse(self, response):
        teacher_lists =response.xpath('//div[@class="teacher_content"]')
        teachers=[]
        for teacher in teacher_lists:
            item = MyscrapyItem()
            image = teacher.xpath("./img/@src").extract()[0]
            name = teacher.xpath('./p/text()|./div/div/text()').extract()[0]
            info = teacher.xpath('./text()').extract()
            info = "".join(info)
            item["teacher_name"] = name
            item["teacher_image"] = image
            item["teacher_info"] = info
            teachers.append(item)
            yield item