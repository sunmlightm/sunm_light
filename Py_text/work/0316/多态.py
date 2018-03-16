class Animal(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("%s正在吃"%self.name)
class Person(object):
    def feed_animal(self,animal):
        animal.eat()

class Dog(Animal):
    def woof(self):
        print("dog is woof")

dog=Dog("bai")
people=Person()
people.feed_animal(dog)