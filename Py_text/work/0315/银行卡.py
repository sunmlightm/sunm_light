# 定义银行卡的类
class BankCard(object):
    # 定义初始化用户名和卡内余额
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    # 定义存款方法
    def money_in(self,money):
        self.balance+=money
        print("%s,您本次存款%d元，卡内金额为%d元"%(self.name,money,self.balance))
    # 定义取款方法
    # 若取款大于卡内余额则无法取出
    # 否则取出金额，卡内减去相应的金额
    def money_out(self,money):
        if self.balance<money:
            print("您的余额不足")
        else:
            self.balance-=money
            print("%s,您本次取款%d元，卡内金额为%d元" % (self.name, money, self.balance))
    # 定义转账方法
    # 转账成功打印出对方账户，转账金额和卡内余额
    def money_give(self,money,card):
        if self.balance<money:
            print("您的余额不足")
        else:
            self.balance-=money
            print("%s,您转账给%s:%d元，卡内金额为%d元" % (self.name, card,money, self.balance))
#创建一个对象
wukong=BankCard("wukong",100)
# 循环操作
while True:
    # 打印操作说明
    print("="*20)
    print("\t1.存款")
    print("\t2.取款")
    print("\t3.转账")
    print("=" * 20)
    num=int(input("请输入你的选项："))
    if num==1:
        money=int(input("请输入存款金额"))
        wukong.money_in(money)
    elif num==2:
        money = int(input("请输入取款金额"))
        wukong.money_out(money)
    elif num==3:
        name=input("请输入对方账户")
        money = int(input("请输入转账金额"))
        wukong.money_give(money,name)
    else:print("请输入正确的选项")