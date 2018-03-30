# 创建静态方法
@staticmethod
def text_2():
    print("静态方法")

# 创建类方法
@classmethod
def text_3(cls):
    print("类方法")

# 使用type创建类
Text=type("Text",(object,),{"name":"庄三","text_2":text_2,"text_3":text_3})

# 自定义方法
def text_1():
    print("实例方法")

#  创建实例对象
text=Text()
# 添加实例方法
text.text_1=text_1
# 调用实例方法
text.text_1()
# 调用静态方法
text.text_2()
# 调用类方法
text.text_3()