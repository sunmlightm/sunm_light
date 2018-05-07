#encoding=utf-8
# @Time    : 5/7/18 12:00 PM
# @Author  : sunml
import urllib.request
response=urllib.request.urlopen('http://www.baidu.com')

response_data=response.read()
print(response_data.decode('utf-8'))