# _*_coding:utf-8_*_
# Author : sunm
# @Time :  19:08
import requests,json,jsonpath

url='http://www.lagou.com/lbs/getAllCitySearchLabels.json'
response=requests.get(url)
data=response.text

dict_str=json.loads(data,encoding='uft-8')
city_list=jsonpath.jsonpath(dict_str,'$..name')
print(city_list)