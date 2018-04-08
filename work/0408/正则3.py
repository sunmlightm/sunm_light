import re
st='''
<img data-original=
"https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"
 src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"
 style="display: inline;">
'''
obj=re.findall("http.*jpg",st)
print(obj)