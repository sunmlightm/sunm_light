# _*_coding:utf-8_*_
# Author : sunm
# @Time :  19:53
from queue import Queue
from threading import Thread
from lxml import etree
import time,requests

crawl_exit = False
parse_exit = False

class ThresdCrawl(Thread):
    def __init__(self,thread_name,page_queue,data_queue):
        super(ThresdCrawl,self).__init__()
        self.thread_name=thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/6.0)"}

    def run(self):
        while not crawl_exit:
            try:
                page=self.page_queue.get(block=False)
                url="https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
                print("%s开始工作了,页数是 %d"%(self.thread_name,page))
                response=requests.get(url,headers=self.headers)
                html= response.text
                self.data_queue.put(html)
                time.sleep(1)
            except Exception as e:
                pass
                break


class ThreadParse(Thread):
    def __init__(self,thread_name, data_queue,file_name,lock):
        super(ThreadParse,self).__init__()
        self.thread_name = thread_name
        self.file_name=file_name
        self.data_queue = data_queue
        self.lock=lock

    def run(self):
        while not parse_exit:
            try:
                html=self.data_queue.get(block=False)
                print("%s开始解析数据:%s" % (self.thread_name,html[:10]))
                self.parse(html)
            except Exception as e:
                pass

    def parse(self,html):
        content=etree.HTML(html)


def main():
    page_queue=Queue(10)
    for page in range(1,11):
        page_queue.put(page)
    data_queue=Queue()
    thread_craws=[]
    thread_names=['采集线程1','采集线程2','采集线程3']
    for thread_name in thread_names:
        crawl=ThresdCrawl(thread_name,page_queue,data_queue)
        crawl.start()
        thread_craws.append(crawl)


if __name__ == '__main__':
    main()