 #encoding=utf-8
# @Time    : 5/8/18 3:07 PM
# @Author  : sunml
import requests

kw={'wd':'尚硅谷'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response=requests.get('https://www.baidu.com/s',params=kw,headers=headers)
print(response.text)