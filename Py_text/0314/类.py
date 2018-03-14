class Students(object):
    def eat(self):
        print("eat")
    def sleep(self,hours):
        print("sleep:%s"%hours)

wang=Students()
wang.eat()
wang.sleep(10)
wang.name="123"
print(wang.name)
print(wang)

li=Students()
print(li.name)