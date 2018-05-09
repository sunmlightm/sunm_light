#encoding=utf-8
# @Time    : 5/8/18 8:51 AM
# @Author  : sunml
from urllib.request import Request,urlopen
from urllib.parse import urlencode

url = "http://httpbin.org/post"
data={'name':'zhangsan','age':'22'}
data=urlencode(data).encode('utf-8')

request=Request(url,data=data)
response=urlopen(request)
data=response.read().decode('utf-8')
print(data)