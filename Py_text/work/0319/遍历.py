try:
    print(num)
    f=open("123","r")

except (NameError,FileNotFoundError):
    print("出错了")
except:
    print("其他错误")
else:"没有错误"