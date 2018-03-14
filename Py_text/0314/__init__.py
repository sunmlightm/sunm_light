class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self,study):
        print("name:%s,age:%s,study:%s"%(self.name,self.age,study))
    def play_ball(self,ball):
        print("name:%s,age:%s,ball:%s"%(self.name,self.age,ball))
stu1=Student("wukong","18")
stu1.age="20"
stu1.study("Chinese")
stu1.play_ball("pingpong")

stu2=Student("bajie","21")
stu2.study("English")
stu2.play_ball("football")