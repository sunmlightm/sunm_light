class Soldler(object):
    def __init__(self,name):
        self.name=name
    def shoot(self,gun):
        gun.shoot()
    def input_num(self,gun):
        gun.input_num()

class Gun(object):
    def __init__(self,real_num,max_num):
        self.real_num=real_num
        self.max_num=max_num
    def shoot(self):
        print("开枪")
        if self.real_num>0:
            self.real_num-=1
            print("当前子弹:%d" % self.real_num)
        else:print("没有子弹了")
    def input_num(self):
        print("上弹")
        self.real_num=self.max_num
        print("当前子弹:%d"%self.real_num)


AK47=Gun(20,20)
xusanduo=Soldler("许三多")
xusanduo.shoot(AK47)
xusanduo.shoot(AK47)
xusanduo.input_num(AK47)
