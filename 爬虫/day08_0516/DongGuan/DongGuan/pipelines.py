# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DongguanPipeline(object):
    def open_spider(self,spider):
        self.file=open('dongguan.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        py_dict = dict(item)
        text = json.dumps(py_dict,ensure_ascii=False) + '\n'
        self.file.write(text)
        return item

    def close_spider(self,spider):
        self.file.close()