# -*- coding: utf-8 -*-
import os

import scrapy
from mysina.items import MysinaItem


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        #返回的是:新闻,体育,娱乐等等大标题列表
        parent_titles = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()
        # 返回的是:新闻,体育,娱乐等等大标题的链接列表
        parent_urls = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()


        #得到小标题的列表
        sub_titles = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()
        #得到小标题对应链接的列表
        sub_urls = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()
        # print(sub_titles)
        #装每个小类的相关信息的集合
        items = []


        for i in range(len(parent_urls)):
            #大类的目录
            parent_file = "./Data/"+parent_titles[i]


            #大类的url:http://news.sina.com.cn/
            parent_url = parent_urls[i]
            for j in range(len(sub_urls)):

                item = MysinaItem()
                #小类的url:http://news.sina.com.cn/china/
                #大类和小类标题前缀相同都是:http://news.sina.com.cn/
                sub_url = sub_urls[j]
                #判断小类的标题是否属于大类标题
                is_belong = sub_url.startswith(parent_url)


                if is_belong:
                    #.Data/新闻/国内,.Data/新闻/国际
                    sub_file = parent_file +"/" +sub_titles[j]
                    #创建目录,先判断目录是否存在,如果不存在再创建目录
                    if not os.path.exists(sub_file):
                        os.makedirs(sub_file)


                    #存储大分类标题和路径
                    item["parent_title"] = parent_file
                    item["parent_urls"] = parent_url

                    #小类的标题和url
                    item["sub_title"] = sub_titles[j]
                    # 小类的标题下链接对应的要存储本地路径
                    item["sub_urls"] = sub_url
                    item["sub_file_name"] = sub_file

                    #添加到字典里面去
                    items.append(item)

        for item in items:
            #得到小类请求的链接,并且发起请求
            sub_urls = item["sub_urls"]
            sub_title = item["sub_title"]

            # print("sub_title==",sub_title)
            # print("sub_urls==",sub_urls)
            #发送每个小类url的Request请求，得到Response连同包含meta数据 一同交给回调函数 second_parse 方法处理
            yield scrapy.Request(url=sub_urls,meta={"meta_item":item},callback=self.second_parse)


    def second_parse(self,response):
        # print(response.url)
        #取出
        meta_item = response.meta["meta_item"]
        # print(item)
        urls = response.xpath("//a/@href").extract()
        items = []
        for url in urls:

            parent_url = meta_item["parent_urls"]

            #判断是否链接是当前类的子链接,判断是否是shtml后缀
            is_belong = url.startswith(parent_url) and url.endswith(".shtml")

            if is_belong:
                item = MysinaItem()
                # 存储大分类标题和路径
                item["parent_title"] = meta_item["parent_title"]
                item["parent_urls"] = meta_item["parent_urls"]

                # 小类的标题和url
                item["sub_title"] = meta_item["sub_title"]
                # 小类的标题下链接对应的要存储本地路径
                item["sub_urls"] = meta_item["sub_urls"]
                item["sub_file_name"] = meta_item["sub_file_name"]

                #本次新添加的
                item["son_urls"] = url

                # 添加到字典里面去
                items.append(item)
                # print(url)

        #对每个文章的链接发起请求
        for item in items:
            #得到文章的链接,并且发起请求
            son_urls = item["son_urls"]

            # print("sub_title==",sub_title)
            # print("sub_urls==",sub_urls)
            #发送每个文章的链接url的Request请求，得到Response连同包含meta数据 一同交给回调函数 detail_parse 方法处理
            yield scrapy.Request(url=son_urls,meta={"meta_item2":item},callback=self.detail_parse)



    def detail_parse(self,response):
        print("son_urls==",response.url)

        item = response.meta["meta_item2"]
        #文章的标题
        head = response.xpath('//h1[@class="main-title"]/text()|//h1[@id="artibodyTitle"]/text()').extract()
        #文章的内容
        content = response.xpath('//div[@class="article"]//p/text()|//div[@id="artibody"]//p/text()').extract()
        # print(head)
        # print(content)

        content = "".join(content)
        print(content)


        item["head"] = head
        item["content"] = content
        yield item
