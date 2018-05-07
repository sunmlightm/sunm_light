#encoding=utf-8
# @Time    : 5/7/18 8:27 PM
# @Author  : sunml
import requests
response=requests.get("http://www.atguigu.com/images/logo.jpg")
if response.status_code==200:
    with open('123.jpg','wb') as f:
        f.write(response.content)
        print('下载完成')