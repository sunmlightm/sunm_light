import types
# 创建Person类
class Person(object):
    # 类属性
    age=20
    # 类方法
    @classmethod
    def class_(cls):
        print("classmethod")

# 创建一个方法
def text(self):
    print(self.age)

# 创建实例对象
person=Person()
# 类调用类方法
Person.class_()
# 对象动态添加有参数方法
person.text=types.MethodType(text,person)
# 调用新添加的方法
person.text()
# 对象调用类属性和方法
print(person.age)
person.class_()