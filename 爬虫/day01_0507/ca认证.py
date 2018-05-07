#encoding=utf-8
# @Time    : 5/7/18 7:11 PM
# @Author  : sunml
from urllib.request import urlopen,Request
import ssl

context=ssl._create_unverified_context()
url='https://www.12306.cn/'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

request=Request(url,headers=headers)
response=urlopen(request,context=context)
print(response.read().decode("utf-8"))