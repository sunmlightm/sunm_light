class Animal(object):
    nick_name="动物"
    color="白"
    age=1
    def eat(self,food):
        print("%s喜欢吃：%s"%(self.nick_name,food))

class Cat(Animal):
    pass
class Dog(Animal):
    pass
class Bird(Animal):
    def __init__(self):
        print("我是一只小小鸟")
    def fly(self):
        print("%s小鸟在飞"%self.nick_name)

cat=Cat()
cat.nick_name="huahua"
cat.eat("fish")
