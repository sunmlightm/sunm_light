#_*_coding:utf-8_*_
#author:sunml
#time:2018/5/99:46
import requests,re
from lxml import etree

class Spider(object):
    def loda_page(self,page):
        url='http://www.neihan8.com/article/list_5_'+str(page)+'.html'
        response=requests.get(url)
        data=response.content.decode('gb2312')
        return data

    def re_data(self,data):
        # pattern = re.compile(r'<div class="f18 mb20">.*?</div>', re.S)
        # data_list = pattern.findall(data)

        html=etree.HTML(data)
        data_list=html.xpath('//div[@class="f18 mb20"]//text()')
        # data_list=etree.tostring(data_list)
        # print(data_list)

        for item in data_list:
            item=item.replace(' ','')
            # item=item.replace('<div class="f18 mb20">',"")\
            # .replace('</div>',"").replace('<p>',"").\
            # replace('</p>',"").replace('<br />',"").\
            # replace('&ldquo;',"").replace('&ldquo;',"")\
            # .replace("&hellip;","").replace("&rdquo;","").replace(' ','')
            print(item)


if __name__ == '__main__':
    spider=Spider()
    data=spider.loda_page(1)
    spider.re_data(data)