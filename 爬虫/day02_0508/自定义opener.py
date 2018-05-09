#encoding=utf-8
# @Time    : 5/8/18 9:56 AM
# @Author  : sunml
from urllib.request import HTTPHandler,Request,build_opener

http_handler=HTTPHandler()
opener=build_opener(http_handler)

url='http://www.baidu.com'
request=Request(url)
response=opener.open(request)

data=response.read().decode('utf-8')
print(data)