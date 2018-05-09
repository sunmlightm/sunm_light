#encoding=utf-8
# @Time    : 5/8/18 4:28 PM
# @Author  : sunml

import requests,re

response=requests.get('http://www.mmjpg.com/hot/')
# print(response.text)
pattern=re.compile(r"http://img.mmjpg.*?jpg")
imgs=pattern.findall(response.text)

# num=1
for img in imgs:
#     img=requests.get(img)
    print(img)
#     print(img.content)
#     # with open(str(num)+'.jpg','wb') as f:
#     #     f.write(imgdown.content)
#     print(str(num)+'ok')
#     num += 1
    res=requests.get(img)
    print(res.content)