# _*_coding:utf-8_*_
# Author : sunm
# @Time :  11:49
from  urllib3 import PoolManager,disable_warnings
from bs4 import BeautifulSoup
import re

disable_warnings()

url = 'https://list.tmall.com/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton'

headers={
"authority":"list.tmall.com",
"method":"GET",
"path":"/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton",
"scheme":"https",
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-XA;q=0.6",
"cache-control":"max-age=0",
"cookie":"hng=CN%7Czh-CN%7CCNY%7C156; lid=huanguang8917; cna=EslUE/LF+lICAXlFUaa7nKeB; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; UM_distinctid=163388bdfc62f7-023f15804f2f3a-f373567-1fa400-163388bdfc78e0; tk_trace=1; uc1=cookie14=UoTeOLn5Ei1MOg%3D%3D; t=48908f515b4ac788abfc9e2f49040989; uc3=nk2=CzhMCY33ve11DR4Z4A%3D%3D&id2=UUpgT77NXTneOA%3D%3D&vt3=F8dBz44jsuUs%2FCjdoI0%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; tracknick=huanguang8917; lgc=huanguang8917; _tb_token_=e61ee15f371e9; cookie2=36f2a2de2628bd144b536212eb8d38b9; enc=nVU26IoA1ueEV4JMQbDS2eTn7Qj2DMW1VrSU3ImOGQ2blae9EI8%2FW1ZuDgWiz4sbOXVZFAh3mTTrgIzNBMwm7g%3D%3D; tt=tmall-main; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; cq=ccp%3D1; swfstore=41766; res=scroll%3A1438*6088-client%3A1438*672-offset%3A1438*6088-screen%3A1920*1080; pnm_cku822=098%23E1hvCpvUvbpvUvCkvvvvvjiPPFdv1jrmnLSw0jljPmP9tjrERLMO0jrbRsqOQjEhRphvChCvvvvPvpvhvv2MMQhCvvXvppvvvvmEvpvVpyUUCC%2BfuphvmhCvCU0euTAuKphv8hCvv2Qvvhv3phvZS9vvpKEvpCQmvvChNhCvjvUvvhBZphvZt9vvp6QEvpCWp2Krv8WBU6rkLuc6V31scsXXiXhpVj%2BOUx8x9EQaWDw6pwethbUf8cyyYnezrmphwHAxfBeXjovZPs0Q%2Bul1p169D76XeB6FNZqv%2B8wCvvBvpvpZ; isg=BOTkVo91YqJu55ZKMiVFlIwrteIW1R3HbJ4cw_4Ffq9yqYRzJo3YdxrLbQGxcUA_",
"dnt":"1",
"referer":"https://www.tmall.com/",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}

http=PoolManager()
response=http.request('GET',url,headers=headers)
data=response.data.decode('GBK')

soup=BeautifulSoup(data,'lxml')
list_links=[]
list_id=[]
tags = soup.find_all(href=re.compile(r'//detail.tmall.com/item.htm'))
for tag in tags:
    list_links.append(tag['href'])
list_links=list(set(list_links))

for link in list_links:
    id=link.split('=')[1].split('&')[0]
    list_id.append(id)
print(list_id)

