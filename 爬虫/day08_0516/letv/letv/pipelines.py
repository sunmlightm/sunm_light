# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.utils.project import get_project_settings
import os
import json


class LetvPipeline(object):
    def open_spider(self, spider):
        print('爬虫执行开始回调')

    def __init__(self):
        self.file = open('letvLive.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item_dict = dict(item)
        json_text = json.dumps(item_dict, ensure_ascii=False) + '\n'
        self.file.write(json_text)
        return item

    def close_spider(self, spider):
        self.file.close()


class LetvImagePipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_path = item['nick_image']
        yield scrapy.Request(image_path)
        # return [Request(x) for x in item.get(self.images_urls_field, [])]

    def item_completed(self, results, item, info):
        # if isinstance(item, dict) or self.images_result_field in item.fields:
        #     item[self.images_result_field] = [x for ok, x in results if ok]
        image_path = [x['path'] for ok, x in results if ok]
        old_name = self.IMAGES_STORE + '/' + image_path[0]
        new_name = self.IMAGES_STORE + '/'+ item['nick_name'] + '.jpg'
        os.rename(old_name, new_name)
        item['image_path'] = new_name

        return item
