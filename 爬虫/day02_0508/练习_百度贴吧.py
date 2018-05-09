#encoding=utf-8
# @Time    : 5/8/18 8:36 AM
# @Author  : sunml
from urllib import parse
from urllib.request import Request,urlopen

'http://tieba.baidu.com/f?kw=%E5%BB%8A%E5%9D%8A%E5%B8%88%E8%8C%83%E5%' \
'AD%A6%E9%99%A2&ie=utf-8&pn=50'


def main():
    kw=input('请输入要查询的贴吧名称')
    startpage=int(input('请输入起始页'))
    endpage=int(input('请输入结束页'))

    kw={'kw':kw}
    kw=parse.urlencode(kw)
    url='http://tieba.baidu.com/f?'+kw
    baidu_spider(url,startpage,endpage)


def baidu_spider(url,startpage,endpage):
    for num in range(startpage,endpage+1):
        pn=(num-1)*50
        newurl=url+'&ie=utf-8&pn='+str(pn)
        down(newurl,num)


def down(url,num):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    request=Request(url,headers=headers)
    response=urlopen(request)
    data=response.read()
    save(data,num)


def save(data,num):
    with open('第'+str(num)+'页.html','wb') as f:
        f.write(data)
    print('第'+str(num)+'页保存成功')


if __name__ == '__main__':
    main()