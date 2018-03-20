# -*-coding:utf-8-*-
'''人类
属性
姓名 name
血量 hp
持有的枪 gun
方法
安装子弹
安装弹夹
拿枪（持有抢）
开枪
'''


class People(object):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.gun = None

    # 安装子弹
    def make_bullet(self, cilp_item, bullet_num):

        cilp_item.save_bullet(bullet_num)

    # 安装弹夹
    def make_cilp(self, gun_item, cilp_item):
        gun_item.save_cilp(cilp_item)

    # 拿枪
    def make_gun(self, take_gun):
        self.gun = take_gun

    # 开枪
    def fire_now(self, other_peoper):
        self.gun.fire(other_peoper)

    # 掉血
    def lose_blood(self, bullet_kill):
        self.hp -= bullet_kill

    def __str__(self):
        if self.gun:
            return "%s他拿着枪，现在的hp是%d" % (self.name, self.hp)
        else:
            if self.hp > 0:

                return "%s没有枪,现在的hp是%d" % (self.name, self.hp)
            else:
                return "%s退出游戏" % (self.name)


'''6.1.2. 枪类
属性
弹夹（默认没有弹夹，需要安装）
方法
连接弹夹（保存弹夹）
射子弹
'''


class Gun(object):
    # 默认属性没有弹夹
    def __init__(self, cilp):
        self.cilp = cilp
        self.cilp = None  # 弹夹为空

    # 链接子弹让子弹保存到弹夹
    def save_cilp(self, cilp_item):
        self.cilp_item = cilp_item

    # 开火
    def fire(self, other_peoper):
        one_butter = self.cilp_item.pop_bullet()
        one_butter.shooting(other_peoper)

    # 测试枪里的子弹数量
    def __str__(self):
        return "%s里有%s发子弹" % (self.cilp, self.cilp_item)


'''6.1.3. 子弹类
属性
杀伤力
方法
伤害敌人(让敌人掉血)
'''


class Bullet(object):
    def __init__(self):
        self.bullet_kill = 20  # bullet_num子弹杀伤力

    # 射击
    def shooting(self, other_peoper):
        other_peoper.lose_blood(self.bullet_kill)


'''6.1.4. 弹夹类
属性
容量（子弹存储的最大值30）
当前保存的子弹
方法
保存子弹（安装子弹的时候）
弹出子弹（开枪的时候）
'''


class Cilp(object):
    def __init__(self, clip_num):
        self.clip_num = clip_num
        self.bullet_item = []  # 设置装子弹的容器

    def save_bullet(self, bullet_num):
        # 装子弹的时候保存到容器
        self.bullet_item.append(bullet_num)

    # 弹出最后一个子弹
    def pop_bullet(self):
        if self.bullet_item:
            return self.bullet_item.pop()
        else:
            return None

    # 测试弹夹有多少发子弹
    def __str__(self):
        return "弹夹%d有%d发子弹" % (len(self.bullet_item), self.clip_num)


def main():
    """主程序入口，主要逻辑都在这里"""

    # １．创建老王一个实例对象\
    laowang = People("老王")

    # ２．创建一个枪的实例对象
    gun = Gun('AK47')
    # ３．创建一个弹夹实例对象
    cilp = Cilp(30)
    for item in range(20):
        # ４．创建一些子弹实例对象
        bullet = Bullet()
        # ５．老王安装子弹到弹夹
        laowang.make_bullet(cilp, bullet)
    # 6.　老王安装弹夹到枪里面
    laowang.make_cilp(gun, cilp)
    # print(gun)
    # print(cilp)
    # 7.创建一个敌人
    guaizi = People("拐子")
    # 8.老王拿枪－－－保存枪到老王里面
    laowang.make_gun(gun)
    print(laowang)
    print(guaizi)
    # 9.老王开枪打拐子
    laowang.fire_now(guaizi)
    print(guaizi)


if __name__ == '__main__':
    main()