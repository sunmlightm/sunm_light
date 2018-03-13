#定义函数
def num_s(num_min,num_max):
    #遍历参数范围内所有的整数（两头的都取到）
    for i in range(num_min,(num_max+1)):
        #设置标志位
        flg=0
        #遍历从２到要判断的数字之间的所有整数
        # 如果余数为０则证明此数字不是素数
        # 将标志位设置为１，跳出次循环
        for j in range(2,i):
            if i%j==0:
                flg=1
                break
        # 若标志位为０意味着此数没有被整除，为素数，并打印这个数
        if flg==0:
            print(i,end=" ")

num_s(100,200)#输入参数执行函数
