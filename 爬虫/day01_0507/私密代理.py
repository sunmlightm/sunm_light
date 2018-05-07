#encoding=utf-8
# @Time    : 5/7/18 8:02 PM
# @Author  : sunml
from urllib.request import build_opener,ProxyHandler,Request


proxy_hander = ProxyHandler({"http":"183.159.81.4:18118"})
opener = build_opener(proxy_hander)

request = Request("http://mm.chinasareview.com/wp-content/uploads/2017a/07/21/05.jpg")
reponse = opener.open(request)
data=reponse.read()
with open('123.jpg','wb') as f:
    f.write(data)

