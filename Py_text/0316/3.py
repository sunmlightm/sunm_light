class Cat(object):
    def __init__(self,name):
        self.name=name
        self.color="yellow"

class Bosi(Cat):
    def __init__(self,name):
        Cat.__init__(self,name)

    def getName(self):
        return self.name

bosi=Bosi("xiaohua")
print(bosi.name)
print(bosi.color)