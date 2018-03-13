f=open("text1.txt","r")
f.seek(-1,2)
value=f.tell()
print(value)