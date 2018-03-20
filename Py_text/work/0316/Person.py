class Person(object):

    def __init__(self,name):
        self.name=name
        self.__age=0
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        age=self.__age
        return age
    def __str__(self):
        msg=str(self.get_age())+'姓名'+self.name
        return msg
class St(Person):
    def __init__(self,name,result):
        super().__init__(name)
        self.result=result

class Wo(Person):
    def __init__(self,name,wage):
        super().__init__(name)
        self.result=wage


st=St("wukong",100)
st.set_age(18)
print(st.get_age())
print(st.name)
print(st.result)
print(st)