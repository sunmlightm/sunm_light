#encoding=utf-8
# @Time    : 5/7/18 7:18 PM
# @Author  : sunml
from urllib import parse
from urllib.request import Request,urlopen


def save(data,num):
    with open('第'+str(num)+'页.html','wb') as f:
        f.write(data)
    print('第'+str(num)+'页下载完毕')

def down(url,num):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request=Request(url,headers=headers)
    response=urlopen(request)
    data=response.read()
    save(data,num)

def baidu_spider(url,startpage,endpage):
    for num in range(startpage,endpage+1):
        pn=(num-1)*50
        url=url+'&ie=utf-8&pn='+str(pn)
        down(url,num)



def main():
    kw=input('请输入要爬取的贴吧:')
    startpage=int(input('请输入起始页'))
    endpage=int(input('请输入结束页'))

    kw={'name':kw}
    kw=parse.urlencode(kw)
    url='https://tieba.baidu.com/f?'+kw
    baidu_spider(url,startpage,endpage)

if __name__ == '__main__':
    main()