class Person(object):
    def __init__(self):
        self.__name="wukong"
        self.__age=18
    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

list=[]
for i in range(0,5):
    person=Person()
    person.set_name("wukong"+str(i))
    list.append(person)
for person in list:
    print(person.get_name())