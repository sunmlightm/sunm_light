import re
while True:
    num=input("请输入电话号码")

    obj=re.match("([0]\d{2,3})-([1-9]\d{6})",num)

    if obj!=None:
        print("电话号码合理")
    else:
        print("您输入的电话号码不合理")