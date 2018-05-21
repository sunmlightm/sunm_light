# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.utils.project import get_project_settings
import pymongo


class DoubanmovietopPipeline(object):
    def __init__(self):
        self.file = open("movies.json",'w',encoding="utf-8")
        host = get_project_settings().get("MOGODB_HOST")
        port = get_project_settings().get("MOGODB_PORT")
        dbname = get_project_settings().get("MONGODB_DBNAME")
        table = get_project_settings().get("MONGODB_SHEETNAME")

        client = pymongo.MongoClient(host=host, port=port)
        dbname = client[dbname]
        self.collections = dbname[table]

    def process_item(self, item, spider):
        python_dict = dict(item)
        json_text = json.dumps(python_dict, ensure_ascii=False) + "\n"
        self.file.write(json_text)
        self.collections.insert(python_dict)
        return item


    def close_spider(self,spider):
        self.file.close()