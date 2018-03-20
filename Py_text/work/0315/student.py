class Students(object):
    def __init__(self,name,age,school):
        self.name=name
        self.age=age
        self.school=school
    def st_eat(self):
        print("%s正在吃饭"%self.name)

    def st_learn(self):
        print("%s正在学习" % self.name)
    def __str__(self):
        msg="学生姓名："+self.name+" 年龄:"+self.age+" 学校："+self.school
        return msg

st1=Students("wukong","18","huaguoshan")
print(st1)