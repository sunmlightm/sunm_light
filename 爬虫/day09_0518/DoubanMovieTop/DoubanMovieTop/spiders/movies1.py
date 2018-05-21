# -*- coding: utf-8 -*-
import scrapy
from DoubanMovieTop.items import DoubanmovietopItem

class Movies1Spider(scrapy.Spider):
    name = 'movies1'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = [url + str(offset) + "&filter="]

    def parse(self, response):
        movies = response.xpath('//div[@class="item"]')
        for movie in movies:
            item = DoubanmovietopItem()
            title = movie.xpath('./div/div/a/span[1]/text()').extract()[0]
            content = movie.xpath('./div/div[@class="bd"]/p/text()').extract()
            content = ''.join(content)
            score = movie.xpath('./div/div[@class="bd"]/div/span[@class="rating_num"]/text()').extract()[0]
            info = movie.xpath('./div/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            info = ''.join(info)
            item["content"] = content
            item["score"] = score
            item["info"] = info
            item["title"] = title
            print(item)
            yield item

        if self.offset<225:
            self.offset+=25
            new_url = self.url + str(self.offset) + "&filter="
            yield scrapy.Request(new_url, callback=self.parse)