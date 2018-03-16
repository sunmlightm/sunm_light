class Plant(object):
    def __init__(self,name):
        self.name=name
    def Print(self):
        print("name:",self.name)
class Flower(Plant):
    color="red"
    def work(self):
        print("正在开花")
class Grass(Plant):
    color="green"
    def work(self):
        print("草绿了")

it=Flower("杜鹃")
it.Print()
print(it.color)
it.work()