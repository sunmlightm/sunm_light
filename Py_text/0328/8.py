def gen():
   i = 0
   while i < 5:
      temp = yield i
      print("temp==",temp)
      i += 1
f = gen()
# next(f)
print(f.send(None))
print(f.send("呵呵1"))
# print(f.send("呵呵2"))