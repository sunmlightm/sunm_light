# -*- coding: utf-8 -*-
import scrapy
import json
from letv.items import LetvItem

#     nick_name=scrapy.Field()
#     nick_image=scrapy.Field()
#     data_linl=scrapy.Field()
#     image_path=scrapy.Field()

class LetvliveSpider(scrapy.Spider):
    name = 'letvLive'
    allowed_domains = ['letv.com']
    page=1
    url = "http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=7.13&channelId=2168&pages="+str(page)+"&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN"
    start_urls = [url]

    def parse(self, response):
        text=response.text
        python_dict=json.loads(text,encoding='utf-8')
        for zhubo in python_dict['body']['result']:
            item = LetvItem()
            nick = zhubo["nick"]
            liveUrl = zhubo["liveUrl"]
            screenshot = zhubo["screenshot"]
            print(",nick==", nick, ",liveUrl==", liveUrl, "==", screenshot)
            item['nick_name'] = nick
            item["nick_image"] = screenshot
            item["data_link"] = liveUrl
            yield item
        if self.page<=10:
            self.page+=1
        url = "http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=7.13&channelId=2168&pages=" + str(self.page) + "&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN"
        yield scrapy.Request(url,callback=self.parse)
