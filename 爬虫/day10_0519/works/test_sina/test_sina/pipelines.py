# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime
class ExamplePipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item

class TestSinaPipeline(object):
    def __init__(self):
        self.file = open("sin.json", 'w', encoding="utf-8")

    def process_item(self, item, spider):
        python_dict = dict(item)
        json_text = json.dumps(python_dict, ensure_ascii=False) + "\n"
        self.file.write(json_text)
        return item

    def close_spider(self, spider):
        self.file.close()

class SinaContentPipeline(object):

    def process_item(self, item, spider):
        python_dict = dict(item)
        parent_son_path = item["parent_son_path"]
        grandson_content = item['grandson_content']
        grandson_url = item["grandson_url"]

        new_file_name = parent_son_path+"/"+grandson_url[7:grandson_url.rfind(".")].replace("/","_")+".txt"
        with open(new_file_name,"w",encoding="utf-8") as f:
            f.write(grandson_content)
        return item