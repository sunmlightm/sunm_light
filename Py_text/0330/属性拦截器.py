class Text(object):
    # 新建属性
    name="wukong"
    age=18
    # 设置属性拦截器
    def __getattribute__(self, item):
        # 设置拦截的属性
        if item=="name":
            return "此属性无法被调用"
        # 返回没有被拦截的属性
        else:
            return object.__getattribute__(self,item)

p=Text()
print(p.name)  #被拦截的属性无法调用
print(p.age)    #没有被拦截的正常调用