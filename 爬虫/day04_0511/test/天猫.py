# _*_coding:utf-8_*_
# Author : sunm
# @Time :  18:17
import requests,re
from bs4 import BeautifulSoup

def get_html():
    url = 'https://list.tmall.com/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&xl=xio_6&from=mallfp..pc_1_suggest&smToken=5abff42f85364330a9d348d75771021d&smSign=4FVAKGk34VDHat2XRo97Wg%3D%3D'
    headers = {
        "authority": "list.tmall.com",
        "method": "GET",
        "path": "/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&xl=xio_6&from=mallfp..pc_1_suggest&smToken=5abff42f85364330a9d348d75771021d&smSign=4FVAKGk34VDHat2XRo97Wg%3D%3D",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-XA;q=0.6",
        "cache-control": "max-age=0",
        "cookie": "hng=CN%7Czh-CN%7CCNY%7C156; lid=huanguang8917; cna=EslUE/LF+lICAXlFUaa7nKeB; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; UM_distinctid=163388bdfc62f7-023f15804f2f3a-f373567-1fa400-163388bdfc78e0; enc=nVU26IoA1ueEV4JMQbDS2eTn7Qj2DMW1VrSU3ImOGQ2blae9EI8%2FW1ZuDgWiz4sbOXVZFAh3mTTrgIzNBMwm7g%3D%3D; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; cq=ccp%3D1; t=48908f515b4ac788abfc9e2f49040989; uc3=nk2=CzhMCY33ve11DR4Z4A%3D%3D&id2=UUpgT77NXTneOA%3D%3D&vt3=F8dBz44jsuUs%2FCjdoI0%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; tracknick=huanguang8917; lgc=huanguang8917; _tb_token_=e5ea40d783b76; cookie2=3273a865fbd99bd0d3cf549882546f5a; swfstore=157848; res=scroll%3A1159*7239-client%3A1159*755-offset%3A1159*7239-screen%3A1920*1080; pnm_cku822=098%23E1hvC9vUvbpvUvCkvvvvvjiPPFdvsj3PPLdwQjrCPmPwzjDbn259zjnbnLsygj3CRphvCvvvvvvPvpvhvv2MMQyCvhQhmz%2BvC0Er1nCl5F%2BSBiVvQbmAdcUSYExrg8g7EcqWaNLUe1ODN%2BBlYV0KHkx%2FQjc6D46XjoPgAnmQ%2Bulz8SLUlnpL%2B3%2BdafmxfXuKuphvmvvv9bhRSHXzkphvC99vvOC0pbyCvm9vvvvMphvU1vvvvy1vpvFPvvm2phCvhRvvvUnvphvppvvvvDHvpvAEvphvC9vhvvCvp8wCvvpvvUmm; isg=BEpKJgcRJHCd3Kj4mCNDhvZFmzAsk9u1ZoDC0dSCZx1lh-hBvMoWpaAdk_Nbd0Yt",
        "dnt": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    response=requests.get(url,headers=headers)
    return response.text

def get_id(soup):
    url_all=soup.find_all(href=re.compile(r'//detail.tmall.com/item.htm?'))
    url_list=[]
    for url in url_all:
        url_list.append(url['href'])
    url_list=list(set(url_list))
    id_list=[]
    for link in url_list:
        id = link.split('=')[1].split('&')[0]
        id_list.append(id)
        print(id)
    return id_list

if __name__ == '__main__':
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    pro_id=get_id(soup)