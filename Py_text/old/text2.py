def sum(num):
    if num==1:
        print(num)
    else:
        return num+sum(num-1)
sum(10)