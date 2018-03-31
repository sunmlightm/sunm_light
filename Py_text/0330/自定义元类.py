class Upper(type):
   def __new__(cls, class_name, class_parents, class_attr):
      new_name = {}
      for name, value in class_attr.items():
         if not name.startswith("__"):
             new_name[name.upper()] = value
      return super(Upper, cls).__new__(cls, class_name,class_parents, new_name)

class Person(object,metaclass=Upper):
   country = "中国"
   def test(self):
      print("我是TEST函数，我被调用了")

#调用
p = Person()
print(p.COUNTRY)
p.TEST()
