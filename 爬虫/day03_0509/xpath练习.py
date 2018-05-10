#_*_coding:utf-8_*_
#author:sunml
#time:2018/5/914:58
from lxml import etree

html=etree.parse('./hello.html')
print(html)

# result=etree.tostring(html)
# print(result.decode('utf-8'))

# print(type(html))

# result = html.xpath('//li')
# print(result)
# result = html.xpath('//li[last()]/a/@href')
# print(result)
result=html.xpath('//li/@class')
print(result)
li_lists=html.xpath('//li[last()-1]/a/text()')
print(li_lists)

"//div[contains(@id, 'qiushi_tag_')]"