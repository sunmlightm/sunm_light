import time
class Animal(object):
    def __init__(self,name):
        print("__init__被调用")
        self.name=name
    def __del__(self):
        print("del",end=" ")
        print("%s"%self.name)

dog=Animal("haha")
time.sleep(3)