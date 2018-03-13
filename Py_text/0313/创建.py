f=open("程序员的自我xiu养.txt","w+")
value=input("hello world")
f.write(value)
value_real=f.read()
if value_real==value:
    print(value)
f.close()