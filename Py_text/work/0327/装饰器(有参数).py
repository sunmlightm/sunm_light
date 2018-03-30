def text_add(func):
    def add(*args,a=20):
        print("起床")
        print("洗漱")
        func(*args,a=20)
    return add

@text_add
def text(*args,a=20):
    for x in args:
        print("动作:"+x)
    print("age:%d"%a)
args=("开电脑","写代码")
text(*args)