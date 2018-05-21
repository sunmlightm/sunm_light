# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysinaPipeline(object):
    def process_item(self, item, spider):
        son_urls = item["son_urls"]
        sub_file_name = item["sub_file_name"]
        content = item["content"]
        # print(son_urls)
        # print(sub_file_name)
        #http://finance.sina.com.cn/money/fund/jjyj/2018-03-26/doc-ifysqxmt7284191.shtml
        #变成是:'finance.sina.com.cn_money_fund_jjyj_2018-03-26_doc-ifysqxmt7284191'

        file_name = son_urls[7:son_urls.rfind(".")].replace("/","_")+".txt"
        with open(sub_file_name +"/" +file_name,"w",encoding="utf-8") as f:
            f.write(content)
        return item