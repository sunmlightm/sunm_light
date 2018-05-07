#encoding=utf-8
# @Time    : 5/7/18 7:05 PM
# @Author  : sunml

import urllib.request
from urllib.parse import urlencode

url = "http://httpbin.org/post"
data={'name':'wukong','age':'20'}
data=urlencode(data).encode('utf-8')

response=urllib.request.urlopen(url,data=data)

response_data=response.read()
print(response_data.decode('utf-8'))