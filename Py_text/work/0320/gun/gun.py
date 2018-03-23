import time
def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
# 创建人类
class Person(object):
    # 初始化姓名,没枪,生命值100
    def __init__(self,name):
        self.name=name
        self.gun=None
        self.hp=100
    # 人的方法:安装子弹
    def input_bullet(self,danjia,bullet,num):
        for i in range(0,num):
            danjia.save_bullet(bullet)
    # 人的方法:安装弹夹
    def input_danjia(self,gun,danjia):
        gun.save_danjia(danjia)
    # 拿枪
    def take_gun(self,gun):
        self.gun=gun
        print("%s拿起%s"%(self.name,self.gun.type))
    # 开枪打敌人(target)
    def shot(self,target):
        if self.gun.danjia.bullet_list:
            self.gun.fire(target)
        else:print("没子弹了")
    # 受伤掉血
    def hurt(self,killability):
        self.hp-=killability
    # 显示人的信息
    def __str__(self):
        if self.gun:
            return "%s有枪,生命值是:%d"%(self.name,self.hp)
        else:
            if self.hp>0:
                return "%s没有枪,生命值是:%d"%(self.name,self.hp)
            else:return "%s已经挂掉了\n%s 孙凤春作业"%(self.name,get_time())

# 创建枪类
class Gun(object):
    # 初始化枪的类型(并且没有弹夹)
    def __init__(self,type):
        self.type=type
        self.danjia=None
    # 安装弹夹
    def save_danjia(self,danjia):
        self.danjia=danjia
    def fire(self,target):
        bullet=self.danjia.out_bullet()
        bullet.sheji(target)
    # 显示枪的信息
    def __str__(self):
        return "%s里有%s"%(self.type,self.danjia)

class DanJia(object):
    def __init__(self,max_num):
        self.max_num=max_num
        self.bullet_list=[]
    def save_bullet(self,bullet):
        self.bullet_list.append(bullet)
    def out_bullet(self):
        if self.bullet_list:
            return self.bullet_list.pop()
        else:return None
#     显示弹夹的信息
    def __str__(self):
        return "弹夹信息:%d/%d"%(len(self.bullet_list),self.max_num)

class Bullet(object):
    #初始化子弹伤害
    def __init__(self,killability):
        self.killability=killability
    def sheji(self,target):
        target.hurt(self.killability)


if __name__=="__main__":
    def main():
        laowang=Person("老王")
        AK47=Gun("AK47")
        danjia=DanJia(30)
        bullet=Bullet(20)
        laosong = Person("敌人")
        laowang.input_bullet(danjia,bullet,5)
        laowang.input_danjia(AK47,danjia)
        laowang.take_gun(AK47)
        print(AK47)
        print(danjia)
        print(laowang)
        print(laosong)

        laowang.shot(laosong)
        print(laosong)
        laowang.shot(laosong)
        print(laosong)
        laowang.shot(laosong)
        print(laosong)
        laowang.shot(laosong)
        print(laosong)
        laowang.shot(laosong)
        print(laosong)
        laowang.shot(laosong)
    main()
