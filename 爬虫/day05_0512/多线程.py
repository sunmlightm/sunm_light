import requests
from queue import Queue
from threading import Thread,Lock
import time
from lxml import  etree
import json

crawl_exit=False
parse_exit=False

class CrawlThread(Thread):
    def __init__(self,thread_name,page_queue,data_queue):
        Thread.__init__(self)
        self.thread_name=thread_name
        self.page_queue=page_queue
        self.data_queue=data_queue
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
		}

    def run(self):
        while crawl_exit == False:
            try:
                page=self.page_queue.get(block=False)
                url = "https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
                response = requests.get(url,headers=self.headers)
                text= response.text
                time.sleep(1)
                self.data_queue.put(text)
                print("[%s]:开始执行了请求,url是==%s" % (self.thread_name, url))
            except Exception as e:
                pass

class ParseThread(Thread):
    def __init__(self,thread_name,data_queue,filename,lock):
        Thread.__init__(self)
        self.thread_name=thread_name
        self.filename=filename
        self.data_queue=data_queue
        self.lock=lock
    def run(self):
        while not parse_exit:
            try:
                data=self.data_queue.get(block=False)
                self.parse_data(data)
            except Exception as e:
                pass

    def parse_data(self, data):
        html = etree.HTML(data)
        all_datas = html.xpath('//div[contains(@id,"qiushi_tag_")]')
        for item in all_datas:
            item_dict = {}
            images = item.xpath('./div/a[@rel="nofollow"]/img/@src')
            names = item.xpath('./div/a/h2/text()')
            contents = item.xpath('./a/div[@class="content"]/span/text()')
            click_numbers = item.xpath('./div/span/i/text()')
            comments = item.xpath('./div/span/a/i/text()')

            if len(images) > 0:
                image = images[0]
            if len(names) > 0:
                name = names[0]

            content = contents[0]
            click = click_numbers[0]
            comment = comments[0]
            item_dict["image"] = image
            item_dict["name"] = name
            item_dict["content"] = content
            item_dict["click"] = click
            item_dict["commont"] = comment

            with self.lock:
                json.dump(item_dict, self.filename, ensure_ascii=False)



def main():
    lock=Lock()
    global crawl_exit
    global parse_exit
    page_queue=Queue(10)
    for page in range(1,11):
        page_queue.put(page)
    data_queue=Queue()
    crawl_threads=[]
    crawl_thread_names=['采集线程1','采集线程2','采集线程3']
    for thread_names in crawl_thread_names:
        crawl_thread = CrawlThread(thread_names,page_queue,data_queue)
        crawl_thread.start()
        crawl_threads.append(crawl_thread)

    filename=open('糗事百科.json','a',encoding='utf-8')
    parse_thread_names=['解析线程1','解析线程2','解析线程3']
    parse_threads=[]
    for parse_name in parse_thread_names:
        parse_thread=ParseThread(parse_name,data_queue,filename,lock)
        parse_thread.start()
        parse_threads.append(parse_thread)
    while not page_queue.empty():
        pass
    crawl_exit=True
    for crawl_thread in crawl_threads:
        crawl_thread.join()

    while not data_queue.empty():
        pass
    parse_exit=True
    for parse_thread in parse_threads:
        parse_thread.join()
    with lock:
        filename.close()
    print('OK。。。')

if __name__ == '__main__':
    main()
