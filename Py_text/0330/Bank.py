import random
import os
import time


# 定义银行类
class Bank(object):
    # 初始化金额
    def __init__(self, money):
        self.money = money

    # 定义存钱方法
    def save_money(self, money):
        self.money += money
        print("余额:", self.money)

    # 定义取钱方法
    def take_money(self, money):
        if money > self.money:
            print("余额不足")
        else:
            self.money -= money
            print("余额:", self.money)

# 创建子进程
pid = os.fork()
p1 = Bank(1000)
p2 = Bank(2000)
# 执行子进程
if pid == 0:
    # 循环执行
    for i in range(10):
        # 生成随机数
        num = random.randint(1, 500)
        # 随机数是奇数则取钱
        if num%2:
            print("p2:")
            p2.take_money(num)
        # 否则存钱
        else:
            print("p2:")
            p2.save_money(num)
        print("=======>",i)
        time.sleep(0.5)

# 执行主进程
elif pid > 0:
    for i in range(10):
        num = random.randint(1, 500)
        if num%2:
            print("p1:")
            p1.take_money(num)
        else:
            print("p1:")
            p1.save_money(num)
        time.sleep(0.5)