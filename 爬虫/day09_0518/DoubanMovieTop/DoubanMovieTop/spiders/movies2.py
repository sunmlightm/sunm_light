# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from DoubanMovieTop.items import DoubanmovietopItem

#<a href="?start=50&amp;filter=">3</a>
class Movies2Spider(CrawlSpider):
    name = 'movies2'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        movies = response.xpath('//div[@class="item"]')
        print(movies,"1"*100)
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