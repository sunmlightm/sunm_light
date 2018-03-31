import functools
# 装饰器
def zhuangshi(func):
    @functools.wraps(func)
    def inner():
        print("inner")
        func()
    return inner

@zhuangshi
# 定义被装饰的函数
def text():
    print("text")

text()
print("__name__:",text.__name__) # 使用wraps之后变回正常
