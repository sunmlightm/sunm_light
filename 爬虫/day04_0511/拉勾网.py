# _*_coding:utf-8_*_
# Author : sunm
# @Time :  16:44
# 需求：我们以拉勾网城市JSON文件 http://www.lagou.com/lbs/getAllCitySearchLabels.json 为例
# 获取所有城市，只需要城市的名称，并且把这些名称保存到city.txt文件中

import requests,jsonpath,json

url='http://www.lagou.com/lbs/getAllCitySearchLabels.json'
text=requests.get(url).text
print(type(text))

python_obj = json.loads(text,encoding='uft-8')
city_names=jsonpath.jsonpath(python_obj,'$..name')
print(city_names)