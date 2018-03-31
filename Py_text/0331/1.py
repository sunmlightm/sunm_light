import random


def zhuangshi(func):
    def inner(name, password, type_="user"):
        if type_ == "user":
            num = random.randint(1000, 9999)
            print(num)
            if input("请输入验证码") == str(num):
                print("验证码正确")
                func(name, password)
        elif type_ == "admin":
            if name == "admin":
                func(name, password)

    return inner


@zhuangshi
def denglu(name, password):
    print("正在验证")
    if (name == "user" and password == 1234) or (name == "admin" and password == 1234):
        print("登陆成功")
    else:
        print("用户名或密码错误")


denglu("admin", 1234, "admin")
