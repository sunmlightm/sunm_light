def num_random():
    import random
    return random.randint(1,50)
num=num_random()
print(num)
i=0
while i<3:
    num_input=int(input('请输入一个数字：'))

    if num_input==num:
        print("您猜对了")
        num_i=i+1
        print("您使用了%d次机会"%num_i)
        break
    i += 1
if i==3:
    print("很抱歉，您的机会用完了")
