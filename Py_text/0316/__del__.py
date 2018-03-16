class Person(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print("%s销毁"%self.name)


p=Person("p")
q=Person("q")
del q
w=p
del p
print("="*20)