# 创建类
class Person(object):
    # 限制添加除name age get_name之外的属性和动态添加对象方法
    __slots__ = ("name","age","get_name")
    def __init__(self):
        self.name="张三"
        self.age=18

# 自定义方法
def get_name():
    print("text")

# 创建实例对象
p=Person()
# 调用属性
print(p.name)
print(p.age)
# 添加对象属性
p.get_name=get_name
p.get_name()
