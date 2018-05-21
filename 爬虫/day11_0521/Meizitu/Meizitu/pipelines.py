# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#导入图片类
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from Meizitu.settings import IMAGES_STORE
import os

class MeizituPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image = item["image"]
        yield scrapy.Request(image)


    def item_completed(self, results, item, info):
        image = [x["path"] for ok, x in results if ok][0]
        print("image--item_completed===",image)
        old_image_name = IMAGES_STORE +"/"+image
        new_image_name = IMAGES_STORE +"/"+ item["image"][7:].replace("/","_")
        print("old_image_name==",old_image_name)
        print("new_image_name==", new_image_name)

        os.rename(old_image_name,new_image_name)

        item["image_path"] = new_image_name

        return item
import json
class MeizituJsonPipeline(object):
    def __init__(self):
        self.f = open("meizitu.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        python_dict = dict(item)
        json_str = json.dumps(python_dict,ensure_ascii=False) +"\n"
        self.f.write(json_str)
        return item

    def close_spider(self,spider):
        self.f.close()
