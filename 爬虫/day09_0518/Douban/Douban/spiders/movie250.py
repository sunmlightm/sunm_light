# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class Movie250Spider(scrapy.Spider):
    name = 'movie250'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = 'https://movie.douban.com/top250?start='

    start_urls = [url+str(offset)]

    def parse(self, response):
        movies = response.xpath('//div[@class="info"]')
        for movie in movies:
            item = DoubanItem()
            title = movie.xpath('.//span[@class="title"][1]/text()').extract()[0]
            content = movie.xpath('.//div[@class="bd"]/p[1]/text()').extract()[0]
            content = "".join(content).strip()
            score = movie.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            info = movie.xpath('.//span[@class="inq"]/text()').extract()


            item['title']=title
            item['content']=content
            item['score']=score
            item['info']=info
            yield item

        if self.offset<250:
            self.offset+=25
            new_url = self.url+str(self.offset)
            yield scrapy.Request(new_url,callback=self.parse)

