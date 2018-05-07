#encoding=utf-8
# @Time    : 5/7/18 4:16 PM
# @Author  : sunml

from urllib import parse
from urllib.request import Request,urlopen

def save(data,num):
    with open("第" + str(num) + "页.html", "wb") as f:
        f.write(data)
    print("第" + str(num) + "页保存完毕!")


def page_downlosd(url,num):
    headers={'User-Agent':'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'}
    request = Request(url,headers=headers)
    reponse=urlopen(request)
    data=reponse.read()
    print(data)
    save(data,num)


def baidu_spider(url,startpage,endpage):
    for num in range(startpage,endpage+1):
        pn=(num-1)*50
        newurl=url+'&ie=utf-8&pn='+str(pn)
        page_downlosd(newurl,num)


def main():
    kw = input('请输入要爬取的贴吧名称:')
    start_page = int(input('请输入起始页'))
    end_page = int(input('请输入结束页'))

    kw={'kw':kw}
    kw=parse.urlencode(kw)

    url='https://tieba.baidu.com/f?'+kw
    baidu_spider(url,start_page,end_page)


if __name__ == '__main__':
    main()