# 列表生成式转换生成器
text1=(x for x in range(3))
for x in text1:
    print(x)

def text2():
    i=0
    while i<10:
        i+=1
        num=yield i
        print(num)
f=text2()
print(f.send(None))
print(f.send("one"))
print(f.send("two"))
print(next(f))
print(next(f))
print(next(f))