import re

st="python = 997,java = 100"
def add(num):
    str_num=num.group()
    real_num=str(int(str_num)+1)
    return real_num
obj=re.sub("\d+",add,st)
print(obj)