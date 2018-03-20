class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Eat(self):
        print("%s正在吃饭"%self.name)
    def Taken(self):
        print("%s要去取经"%self.name)
class SunWukong(Person):
    weapon="金箍棒"
    def work(self):
        print("悟空正在除妖")
class ZhuBajie(Person):
    wife="嫦娥"
    def work(self):
        print("八戒正在牵马")
class ShaHeshang(Person):
    home="流沙河"
    def work(self):
        print("沙僧正在挑行李")
wukong=SunWukong("悟空",500)
bajie=ZhuBajie("八戒",300)
shaseng=ShaHeshang("沙僧",300)

print(wukong.name,wukong.age,wukong.weapon)
wukong.Eat()
wukong.work()