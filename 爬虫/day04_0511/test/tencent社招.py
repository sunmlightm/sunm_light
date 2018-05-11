# _*_coding:utf-8_*_
# Author : sunm
# @Time :  18:55
import requests,os
from bs4 import BeautifulSoup

def get_html():
    num = 1
    start = (num - 1) * 10
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    url = 'https://hr.tencent.com/position.php?&start=' + str(start) + '#a'
    response = requests.get(url, headers=headers)
    return response.text


def get_data(soup):
    even_list=soup.select('.even')
    odd_list=soup.select('.odd')
    all_lis=even_list+odd_list
    data_list=[]
    for data in all_lis:
        item = {}
        item['name'] = data.a.get_text()
        item['data_link'] = data.a.attrs['href']
        item['job_category'] = data.select('td')[1].get_text()
        item['recruit_number'] = data.select('td')[2].get_text()
        item['address'] = data.select('td')[3].get_text()
        item['publish_time'] = data.select('td')[4].get_text()
        data_list.append(item)
    return data_list


def save_date(data):
    if os.path.exists('./text') == False:
        os.mkdir('./text')
    with open('./text/json.txt','w') as f:
        f.write(str(data))

if __name__ == '__main__':
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    datalist=get_data(soup)
    save_date(datalist)