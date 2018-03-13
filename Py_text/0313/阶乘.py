def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)
num_c=int(input("请输入一个数字"))
print(factorial(num_c))

def fac_add(a,b,*args):
    if len(args)==0:
        return a+b
    else:
        sum=a+b
        for num in args:
            sum=sum+num
        return sum
num_a=eval(input("请输入一个匿名函数"))

print(fac_add(1,2))