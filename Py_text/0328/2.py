#定义一个函数完成包裹数据<b>xxx</b>
def make_b(func):
   def func_in():
      result = "<b>" + func() +"</b>"
      return result
   return func_in

#定义一个函数完成包裹数据<i>xxx</i>
def make_i(func):
   def func_in():
      result = "<i>" + func() +"</i>"
      return result
   return func_in


@make_b
def test1():
   result = "hell test1"
   return result
@make_i
def test2():
   result = "hell test2"
   return result
@make_b
@make_i
def test3():
   result = "hello test3"
   return result
print(test1())
print(test2())
print(test3())
