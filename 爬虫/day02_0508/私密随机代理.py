#encoding=utf-8
# @Time    : 5/8/18 10:50 AM
# @Author  : sunml
from urllib.request import build_opener,Request,ProxyHandler,HTTPHandler
import random

proxy_list=[

    {'http':'49.79.193.112:61234'},
]

proxy_ip=random.choice(proxy_list)

proxy_handler=ProxyHandler(proxy_ip)
proxy_handler_null=ProxyHandler({})

is_proxy=True

if is_proxy:
    opener=build_opener(proxy_handler)
else:
    opener=build_opener(proxy_handler_null)

url='http://www.baidu.com/'
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

request=Request(url,headers=headers)
response=opener.open(request)
print(response.read().decode('utf-8'))