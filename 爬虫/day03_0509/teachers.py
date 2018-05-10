#_*_coding:utf-8_*_
#author:sunml
#time:2018/5/917:52
import requests
from lxml import etree
from urllib import parse
from urllib.request import Request,urlopen
import os


def save(data):
    num = 1
    request = Request(data)
    response = urlopen(request)
    data = response.read()
    if not os.path.exists("./image/"):
        os.makedirs('./image/')
    with open('第'+str(num)+"张图片.jpg",'wb') as f:
        f.write(data)
        print('第'+str(num)+"张图片.jpg下载完成")
        num += 1

def get_image_url(url):
    request = Request(url)
    response = urlopen(request)
    data = response.read()
    content = data.decode()
    html = etree.HTML(content)
    list_links = html.xpath('//div[@class=“media_bigpic_wrap"]/img/@src')
    for link in list_links:
        print(link)
        save(link)

def get_tieba_link(data):
    content = data.decode()
    html = etree.HTML(content)
    list_links = html.xpath("//div[@class='threadlist_title pull_left j_th_tit']/a/@href")
    for link in list_links:
        url = "https://tieba.baidu.com"+link
        print(url)
        get_image_url(url)

def page_download(newurl):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    request = Request(newurl)
    response = urlopen(request)
    data = response.read()
    get_tieba_link(data)

def baidu_spider(url,startpage,endpage):
    for num in range(startpage,endpage+1):
        pn = (num-1)*50
        newurl = url+'&ie=utf-8&pn='+str(pn)
        page_download(newurl)

def main():
    kw = input("请输入抓取的贴吧名称：")
    startpage = int(input("请输入要抓取的起始页："))
    endpage= int(input("请输入要抓取的结束页："))


    kw = {"kw":kw}
    kw = parse.urlencode(kw)
    url = "http://tieba.baidu.com/f?"+kw
    baidu_spider(url, startpage, endpage)


if __name__ =="__main__":
    main()