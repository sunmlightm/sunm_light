#encoding=utf-8
# @Time    : 5/7/18 4:16 PM
# @Author  : sunml
# //div[@class="threadlist_title pull_left j_th_tit"]//a/@href
# https://tieba.baidu.com/p/5689218997
# //div[@class="d_post_content j_d_post_content"]/img/@src
from urllib import parse
from urllib.request import Request,urlopen
from lxml import etree
import re
num=0

def get_tieab_link(data):
    print("开始下载图片")
    content=data.decode()
    html=etree.HTML(content)
    list_link=html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]//a/@href')
    for link in list_link:
        url='https://tieba.baidu.com'+link
        get_img_url(url)


def get_img_url(url):
    global num
    request=Request(url)
    response=urlopen(request)
    data=response.read()
    content = data.decode()
    html = etree.HTML(content)
    list_link=html.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src')
    print(list_link)
    for img_url in list_link:
        print(img_url)
        num+=1
        nums=num
        # down_img(img_url,nums)


def down_img(url,nums):
    request=Request(url)
    response=urlopen(request)
    data=response.read()
    with open("第"+str(nums)+"张图片.jpg",'wb') as f:
        f.write(data)
        print("第" + str(nums) + "张图片..OK")


def page_downlosd(url,num):
    headers={'User-Agent':'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'}
    request = Request(url)
    reponse=urlopen(request)
    data=reponse.read()
    get_tieab_link(data)


def baidu_spider(url,startpage,endpage):
    for num in range(startpage,endpage+1):
        pn=(num-1)*50
        newurl=url+'&ie=utf-8&pn='+str(pn)
        page_downlosd(newurl,num)


def main():
    print('加载url...')
    # kw = input('请输入要爬取的贴吧名称:')
    kw = '尚硅谷'
    # start_page = int(input('请输入起始页'))
    # end_page = int(input('请输入结束页'))
    start_page = 1
    end_page = 1
    kw={'kw':kw}
    kw=parse.urlencode(kw)
    url='https://tieba.baidu.com/f?'+kw
    baidu_spider(url,start_page,end_page)


if __name__ == '__main__':
    main()