#encoding=utf-8
# @Time    : 5/7/18 2:50 PM
# @Author  : sunml

from urllib.request import Request,urlopen
import random

url='http://sunmlight.top'
headers=[
    {'User-Agent':'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'},
    {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"},
    {'User-Agent':'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)'}
    ]
userAgent=random.choice(headers)
request=Request(url,headers=userAgent)
response=urlopen(request)
response_data=response.read()
print(response_data.decode("utf-8"))
