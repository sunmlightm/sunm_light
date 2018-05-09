#encoding=utf-8
# @Time    : 5/8/18 12:03 PM
# @Author  : sunml
from urllib.request import Request,urlopen

headers={ "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
 "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-XA;q=0.6",
 "Cache-Control":"max-age=0",
 "Connection":"keep-alive",
 "Cookie":"unpl=V2_ZzNtbRJXQ0J1W0BdLBtaVmIKE1sRXkFFcl0WByhKDAdmUEUOclRCFXwUR1BnGFoUZwIZXktcQRdFCHZXfBpaAmEBFl5yAR1LI1USFi9JH1c%2bbUgbF0tAFX0JQlBzHV8NVzMRXXJXQiV1DEVWch5YDWACEltCVEIVcgpAUn4cWjVXBCJtclRBEHIOR2R6KV01JVdOX0tRShZwRUZQeBtVAmMLFVxCUUMWdAhBVn0fWQBhMxNtQQ%3d%3d; __jdu=15238659601712016377447; __jdv=122270672|baidu|-|organic|not set|1525660176112; pin=sunmpa; _tp=J0QGhv3KOdYiBmKDtoj22w%3D%3D; _pst=sunmpa; unick=sunmpa; pinId=9DvsjAJZAy4; PCSYCityID=1; user-key=c2f76e21-2343-461f-ab93-bef9313249f3; cn=0; userInfoaccountclouds=1; __jda=122270672.15238659601712016377447.1523865960.1525751537.1525777649.6; 3AB9D23F7A4B3C9B=MWN5HU3DVINOZIOYDQRGHUBMSOKE2XOYGOVFXVIYHY63P7C3I5NDAIL6YLIJZBOOTLVEE7WA2OKPKTYFTMTUPWBJ4I; _jrda=1; wlfstk_smdl=f0czrw9p464b7pavb03mmuswtjclqla5; __jdc=122270672; _jrdb=1525777765824; TrackID=11DpHLXyGzKO9Sq6qWdaF4cOxGXrZ_o9Qd4vuim1Ho4ATCEe3QczCF3-LfBScEz1XnGGJ5r2ocWjwPBpWkOXpCS89ndvcfC0aGwCkJwnfBgk; thor=B932DB4B7DF93A8C73436F42146DA0710D40B68C9D97CA961BBD735EB06A2228F6477EC5512A1B0E1F5C5490A57FC43C8322D237BB8A6062053CAB215B012AA25ABC12A94276D332FF53738B0AA680948BE52F33BE1D42A8AB14EFF4DA4D165F45FCE38F95C7F5B489B905802A7A9D314C8FC961FB521A0F4BE125A91FFDA1B6; ceshi3.com=000; __jdb=122270672.14.15238659601712016377447|6.1525777649",
 "DNT":"1",
 "Host":"home.jd.com",
 "Upgrade-Insecure-Requests":"1",
 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",}

requrst=Request('https://home.jd.com/',headers=headers)
response=urlopen(requrst)
print(response.read().decode('utf-8'))