# -*- coding: utf-8 -*-
import os
import requests
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Meizi2.settings import IMAGES_STORE

class Meizi2Pipeline(object):
    def process_item(self, item, spider):
        if 'images' in item:
            print('有item--image')
            if not os.path.exists(IMAGES_STORE):
                os.makedirs(IMAGES_STORE)

            for image in item['images']:
                image_path = IMAGES_STORE+'/'+image[7:].replace('/','_')

                response = requests.get(image)
                if response.status_code == 200:
                    with open(image_path,'wb') as f:
                        f.write(response.content)

                else:
                    print('图片下载失败:',image)

        return item
