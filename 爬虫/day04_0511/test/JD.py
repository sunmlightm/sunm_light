# _*_coding:utf-8_*_
# Author : sunm
# @Time :  18:42
# _*_coding:utf-8_*_
# Author : sunm
# @Time :  18:17
import requests,re
from bs4 import BeautifulSoup

def get_html():
    url = 'https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&wq=%E8%83%B8%E7%BD%A9&pvid=79709ef405fa45e2bbc253e9fc12213b'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "unpl=V2_ZzNtbRJXQ0J1W0BdLBtaVmIKE1sRXkFFcl0WByhKDAdmUEUOclRCFXwUR1BnGFoUZwIZXktcQRdFCHZXfBpaAmEBFl5yAR1LI1USFi9JH1c%2bbUgbF0tAFX0JQlBzHV8NVzMRXXJXQiV1DEVWch5YDWACEltCVEIVcgpAUn4cWjVXBCJtclRBEHIOR2R6KV01JVdOX0tRShZwRUZQeBtVAmMLFVxCUUMWdAhBVn0fWQBhMxNtQQ%3d%3d; __jdu=15238659601712016377447; __jdv=122270672|baidu|-|organic|not set|1525660176112; pin=sunmpa; _tp=J0QGhv3KOdYiBmKDtoj22w%3D%3D; _pst=sunmpa; unick=sunmpa; pinId=9DvsjAJZAy4; PCSYCityID=1; user-key=c2f76e21-2343-461f-ab93-bef9313249f3; cn=0; 3AB9D23F7A4B3C9B=MWN5HU3DVINOZIOYDQRGHUBMSOKE2XOYGOVFXVIYHY63P7C3I5NDAIL6YLIJZBOOTLVEE7WA2OKPKTYFTMTUPWBJ4I; _jrda=1; TrackID=11DpHLXyGzKO9Sq6qWdaF4cOxGXrZ_o9Qd4vuim1Ho4ATCEe3QczCF3-LfBScEz1XnGGJ5r2ocWjwPBpWkOXpCS89ndvcfC0aGwCkJwnfBgk; __jda=122270672.15238659601712016377447.1523865960.1525777649.1526035369.7; __jdc=122270672; shshshfp=63984738ce65e6ce1b5713127eef6db0; shshshfpa=af7c1083-7a0a-3083-a3cb-973f2ec797b0-1526035370; shshshsID=058023126f6c77b58df8611d4e3c9868_1_1526035370640; shshshfpb=1ff24ea758da149f5a41d404d2cc86c89743e9737ad7d27f85af573a83; xtest=5700.cf6b6759; ipLoc-djd=1-72-2799-0; __jdb=122270672.2.15238659601712016377447|7.1526035369; qrsc=1; rkv=V0600",
        "DNT": "1",
        "Host": "search.jd.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    response=requests.get(url,headers=headers)
    return response.content.decode('utf-8')


def get_id(soup):
    url_all=soup.find_all(href=re.compile(r'//item.jd.com/'))
    url_list=[]
    for url in url_all:
        url_list.append(url['href'])
    url_list=list(set(url_list))
    id_list=[]
    for link in url_list:
        id = link[14:-1].split('.')[0]
        id_list.append(id)
        print(id)
    return id_list

if __name__ == '__main__':
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    pro_id=get_id(soup)