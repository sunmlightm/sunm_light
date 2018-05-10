import re
title = u'你好，hello，世界'
text=re.findall(r'[\u4e00-\u9fa5]+',title,re.S)
print(text)
