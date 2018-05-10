#_*_coding:utf-8_*_
#author:sunml
#time:2018/5/917:38
import requests,os,re

def get_html():
    response=requests.get('http://www.atguigu.com/teacher.shtml')
    data=response.content.decode()
    return data

def get_img(data):
    if os.path.exists(r'./image')==False:
        os.mkdir('image')
    name_list=[]
    datalist=re.findall('<div class="teacher_content".*?</div>',data,re.S)
    for datas in datalist:
        reobject=re.search('<img src=".*jpg">',datas).group()
        img=reobject.split('"')[1]
        img_url = 'http://www.atguigu.com/' + img
        name = img.split('/')[1].split('.')[0]
        response=requests.get(img_url)
        name_list.append(name)
        with open('./image/'+name+'.jpg','wb') as f:
            f.write(response.content)
            print(name+'.jpg...OK')
    get_text(data, name_list)

def get_text(data,name_list):
    data_all=re.search('<div class="teacher_content".*</div>',data,re.S).group()
    datalist=re.findall('jpg.*?img',data_all,re.S)
    if os.path.exists(r'./text')==False:
        os.mkdir('text')
    num=0
    for datas in datalist:
        text = datas.replace('jpg">','').replace('<div class="weibo"><div class="l">','').\
            replace('<span class="teacherfont">','').replace('</div>','').\
            replace('<p style="padding-top:10px;">','').replace('<img','').replace('<p>','').\
            replace('</p>','').replace('<div class="teacher_content">','').replace('<div class="r">','').replace('<br/>','')

        name = name_list[num]
        with open('./text/' + name + '.txt', 'w') as f:
            f.write(text)
            print(name + '.txt...OK')
        num += 1

if __name__ == '__main__':
    data=get_html()
    get_img(data)

