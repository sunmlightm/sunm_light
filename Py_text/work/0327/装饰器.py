import time

def text_add(func):
    print("text_add")
    def add():
        print("add")
        func()
    return add

@text_add
def text():
   print("text")

text()