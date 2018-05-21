# -*- coding: utf-8 -*-
import re

import scrapy
import os


from test_sina.items import TestSinaItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class SinaSpider(CrawlSpider):
    name = 'sina2'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    # http://ent.sina.com.cn/star/
    rules = (
        Rule(LinkExtractor(allow=r'http://news.sina.com.cn/.+?/$'), callback='news_item', follow=False),
        Rule(LinkExtractor(allow=r'http://sports.sina.com.cn/.+?/$'), callback='sports_item', follow=False),
        Rule(LinkExtractor(allow=r'http://ent.sina.com.cn/.+?/$'), callback='ent_item', follow=False),
    )

    #第三层的数据,帖子的数据:标题和内容
    def detail_parse(self,response):
        print("response.url==", response.url)
        item = response.meta["meta_item2"]
        # print("meta_item2==",meta_item2)
        #帖子的标题
        grandson_title = response.xpath('//h1[@id="artibodyTitle"]/text()|//h1[@class="main-title"]/text()').extract()
        grandson_title = ''.join(grandson_title)

        grandson_content = response.xpath('//div[@id="article"]/p[position()>1]/text()|//div[@id="artibody"]/p/text()').extract()
        grandson_content = "".join(grandson_content)

        item["grandson_title"] = grandson_title
        item["grandson_content"] = grandson_content

        print("grandson_content==",grandson_content)
        yield item





    #新闻
    def news_item(self, response):
        print("-" * 20)
        print("response.url--==",response.url)

        # <title>社会新闻_新闻中心_新浪网</title>-->  社会新闻_新闻中心_新浪网
        son_titles  = response.xpath("//title/text()").extract()
        print("titles==",son_titles)
        son_title = ""

        if len(son_titles) > 0:
            # 社会新闻_新闻中心_新浪网 -->社会新闻
            # son_title = son_titles[0][:4]  # 社会新闻

            # 社会新闻_新闻中心_新浪网-->[社会新闻,新闻中心,新浪网]
            son_title = re.split(r'[_|]', son_titles[0])
            son_title = son_title[0]  # 社会新闻
            print("son_title===", son_title)


        # print("meta_item===",meta_item)

        # 得到当前页面所以的链接
        url_list = response.xpath('//a/@href').extract()
        print(url_list)

        if len(url_list) > 0:

            parent_title = "./Date/新闻" + "/" + son_title
            # 没有目录就创建
            if not os.path.exists(parent_title):
                os.makedirs(parent_title)

            print(parent_title)
        else:
            print("当前页面没有路径.....")
        items = []
        for url in url_list:
            parent_url = "http://news.sina.com.cn/"
            # 判断前缀和后缀---判断帖子
            if url.startswith(parent_url) and url.endswith(".shtml"):
                # print("url===", url)
                grandson_url = url
                item = TestSinaItem()
                item["parent_title"] = "新闻"
                item["parent_url"] = "http://news.sina.com.cn/"
                item["son_title"] = son_title
                item["son_url"] = response.url
                item["parent_son_path"] = parent_title
                # 帖子的link
                item["grandson_url"] = grandson_url
                # 添加到列表里面
                items.append(item)

        #打印数据
        print(items)

        # # 请求第三层的链接--帖子的链接
        for item in items:
            grandson_url = item["grandson_url"]
            yield scrapy.Request(grandson_url, callback=self.detail_parse, meta={"meta_item2": item})



    # 体育
    def sports_item(self, response):
        print("-" * 20)
        print("response.url--==", response.url)
        print("response.status--==", response.status)

        # <title>社会新闻_新闻中心_新浪网</title>-->  社会新闻_新闻中心_新浪网
        son_titles = response.xpath("//title/text()").extract()
        print("titles==", son_titles)
        son_title = ""

        if len(son_titles) > 0:
            # 社会新闻_新闻中心_新浪网 -->社会新闻
            # son_title = son_titles[0][:4]  # 社会新闻

            #社会新闻_新闻中心_新浪网-->[社会新闻,新闻中心,新浪网]
            son_title = re.split(r'[_|]',son_titles[0])
            son_title = son_title[0]#社会新闻
            print("son_title===",son_title)



        # 得到当前页面所以的链接
        url_list = response.xpath('//a/@href').extract()
        print(url_list)

        if len(url_list)> 0:
            parent_title = "./Date/体育" + "/" + son_title
            # 没有目录就创建
            if not os.path.exists(parent_title):
                os.makedirs(parent_title)

            print(parent_title)
        else:
            print("当前页面没有路径.....")

        items = []
        for url in url_list:
            parent_url = "http://sports.sina.com.cn/"
            # 判断前缀和后缀---判断帖子
            if url.startswith(parent_url) and url.endswith(".shtml"):
                # print("url===", url)
                grandson_url = url
                item = TestSinaItem()
                item["parent_title"] = "体育"
                item["parent_url"] = parent_url
                item["son_title"] = son_title
                item["son_url"] = response.url
                item["parent_son_path"] = parent_title
                # 帖子的link
                item["grandson_url"] = grandson_url
                # 添加到列表里面
                items.append(item)

        # 打印数据
        print(items)

        # # 请求第三层的链接--帖子的链接
        for item in items:
            grandson_url = item["grandson_url"]
            yield scrapy.Request(grandson_url, callback=self.detail_parse, meta={"meta_item2": item})


    def ent_item(self, response):
        son_titles = response.xpath("//title/text()").extract()
        son_title = ""

        if len(son_titles) > 0:
            son_title = re.split(r'[_|]',son_titles[0])
            son_title = son_title[0]
            print("son_title===",son_title)

        url_list = response.xpath('//a/@href').extract()

        if len(url_list)> 0:
            parent_title = "./Date/娱乐" + "/" + son_title
            if not os.path.exists(parent_title):
                os.makedirs(parent_title)
            print(parent_title)
        else:
            print("当前页面没有路径.....")

        items = []
        for url in url_list:
            parent_url = "http://sports.sina.com.cn/"
            if url.startswith(parent_url) and url.endswith(".shtml"):
                grandson_url = url
                item = TestSinaItem()
                item["parent_title"] = "娱乐"
                item["parent_url"] = parent_url
                item["son_title"] = son_title
                item["son_url"] = response.url
                item["parent_son_path"] = parent_title
                item["grandson_url"] = grandson_url
                items.append(item)

        print(items)

        for item in items:
            grandson_url = item["grandson_url"]
            yield scrapy.Request(grandson_url, callback=self.detail_parse, meta={"meta_item2": item})





