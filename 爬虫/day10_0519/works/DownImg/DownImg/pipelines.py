# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from DownImg.settings import IMAGES_STORE
import os
import requests


class DownimgPipeline(object):
    headers = {
        "Host": "mm.chinasareview.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.meizitu.com/a/5548.html",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "__jsluid=6dad86b537349828028bbed3237da97a",
    }


    def process_item(self, item, spider):
        if "images" in item:
            if os.path.exists(IMAGES_STORE)==False:
                os.makedirs(IMAGES_STORE)
            image_paths = []

            for image in item['images']:
                image_path = IMAGES_STORE + "/" + image[7:].replace("/", "_")
                image_paths.append(image_path)

                if os.path.exists(image_path):
                    continue

                response = requests.get(image,headers=self.headers)
                if response.status_code == 200:
                    with open(image_path,'wb') as f:
                        f.write(response.content)
            item['item_paths']=image_paths
        return item
