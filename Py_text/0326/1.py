class Person(object):
    def __init__(self):
        self._name="wukong"
        self.__age=18
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

    age=property(get_age,set_age)

person=Person()
person.age=20
print(person.age)