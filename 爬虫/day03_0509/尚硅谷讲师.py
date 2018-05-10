#_*_coding:utf-8_*_
#author:sunml
#time:2018/5/917:38
import requests,os
from lxml import etree

def get_html():
    response=requests.get('http://www.atguigu.com/teacher.shtml')
    html=etree.HTML(response.content)
    return html

def get_img(html):
    img_list=html.xpath('//div[@class="teacher_content"]/img/@src')
    name_list=[]
    if os.path.exists(r'./image')==False:
        os.mkdir('image')
    for img in img_list:
        img_url='http://www.atguigu.com/'+img
        response = requests.get(img_url)
        name=img.split('/')[1].split('.')[0]
        name_list.append(name)
        with open('./image/'+name+'.jpg','wb') as f:
            f.write(response.content)
            print(name+'.jpg...OK')
    get_text(html,name_list)

def get_text(html,name_list):
    flg=0
    text_list=[]
    for num in range(1,len(name_list)+1):
        text=html.xpath('//div[@class="teacher_content"]['+str(num)+']//text()')
        text_list.append(text)
    if os.path.exists(r'./text')==False:
        os.mkdir('text')
    for texts in text_list:
        strs=''
        for text in texts:
            strs+=text
        name=name_list[flg]
        with open('./text/'+name+'.txt','w') as f:
            f.write(strs.replace(' ',''))
            print(name+'.txt...OK')
        flg+=1


if __name__ == '__main__':
    html=get_html()
    get_img(html)
