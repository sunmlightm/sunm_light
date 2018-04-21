import redis,MysqlHelper
from hashlib import sha1

red =redis.StrictRedis(host="localhost",port=6379)

name=input("请输入登录名:")
password=sha1(input("请输入密码:").encode()).hexdigest()

uname = red.get("uname")
upwd = red.get("upwd")
if uname and upwd:
    uname=uname.decode("utf-8")
    upwd=upwd.decode("utf-8")
if str(uname) == name:
    if str(upwd)==password:
        print("登陆成功")
    else:print("redis库密码错误")
else:
    helper = MysqlHelper.MysqlHelper(host='localhost')

    result = helper.get_one('select uname,upwd from userinfos where uname=%s', [name])
    try:
        if name == result[0] and password == result[1]:
            print("登录成功")
            red.set("uname",name)
            red.set("upwd",password)
            print("写入redis库成功")
        else:
            print("密码或者账号错误")
    except Exception as result:
        print("账号不存在")

print(red.scan())
print(red.set("name","123"))
print(red.get("name"))
