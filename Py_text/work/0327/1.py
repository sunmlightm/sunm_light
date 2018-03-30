def text_add(func):
    def add(a,*args):
        print("add")
        for x in args:
            print(x)
        func(a=10)
    return add

@text_add
def text(a=10):
    print("text")
    print(a)

args=(1,2,3)
text(a=10,*args)