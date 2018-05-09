#encoding=utf-8
# @Time    : 5/8/18 4:20 PM
# @Author  : sunml

import requests

url='http://www.atguigu.com/pics1/teacherbanner.jpg'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response=requests.get(url,headers=headers)

if response.status_code==200:
    with open('123.jpg','wb') as f:
        f.write(response.content)
    print('ok')