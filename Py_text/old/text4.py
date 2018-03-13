# 定义年份判断函数
def year_r(year):
    # 若能被400整除或者能被4整除，但是不能被100整除的年份表示是闰年
    # 打印"您输入的是闰年"
    # 若不满足条件打印"您输入的不是闰年"
    if (year%400==0)or((year%4==0)and(year%100!=0)):
        print("您输入的是闰年")
    else:print("您输入的不是闰年")
# 循环执行输入年份，判断函数
while True:
    year=int(input("请输入年份:"))
    year_r(year)