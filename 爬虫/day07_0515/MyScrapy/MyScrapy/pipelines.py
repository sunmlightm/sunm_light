# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyscrapyPipeline(object):
    def open_spider(self, spider):
        self.file = open("atgugiu_teacher.json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        print("type(item)==", type(item))
        print("item==", item)
        item_dict = dict(item)
        json_text = json.dumps(item_dict, ensure_ascii=False) + "\n"
        self.file.write(json_text)
        return item

    def close_spider(self, spider):
        print("当爬虫执行结束的时候回调:close_spider")
        self.file.close()