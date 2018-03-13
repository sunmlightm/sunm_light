def mul_99(num):
    i=0
    while i<num:
        for j in range(1,10):
            for k in range(1,j+1):
                print("%d*%d=%d"%(j,k,j*k),end=' ')
            print('')
        i+=1
num=int(input("请输入要打印的次数："))
mul_99(num)