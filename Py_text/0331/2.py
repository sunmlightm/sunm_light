import random


def support_register(func):
    def code(name, password, id):
        security_code = random.randint(1000, 10000)
        if id == "normal":
            print("验证码：", security_code)
            input_code = int(input("请输入验证码："))
            if input_code == security_code:
                print("验证码输入正确")
                func(name, password, id)
            else:
                print("验证码输入错误")
        elif id == "admin":
            print("管理员登陆成功")
            func(name, password, id)

    return code


# name = input("请输入用户名：")
# password = input("请输入密码：")
# id = input("您的身份（normal或者vip）：")
@support_register
def register(name, password, id):
    if name == "wangwei" and password == "123456":
        print("登陆成功")
        print(id)
    else:
        print("用户名或者密码错误，登录失败")


register("wangwei", "123456", "admin")
