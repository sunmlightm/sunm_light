def num_random():
    import random
    num =random.randint(1,3)
    i = 0
    while i < 3:
        num_input = int(input('请输入一个数字：'))
        if num_input == num:
            break
        i += 1
    return i
num_i=num_random()
if num_i<3:
    num_1=num_i+1
    print("您猜对了")
    print("您使用了%d次机会" % num_1)
if num_i==3:
    print("很抱歉，您的机会用完了")

