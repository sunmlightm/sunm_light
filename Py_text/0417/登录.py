import MysqlHelper
import hashlib

helper = MysqlHelper.MysqlHelper(host='192.168.153.134')
name = input("请输入你注册的账号:")
password = input("请输入你的密码:")
password = hashlib.sha1(password.encode("utf-8")).hexdigest()

result = helper.get_one('select uname,upwd from userinfos where uname=%s',[name])
try:
   if name==result[0] and password==result[1]:
      print("登录成功")
   else:
      print("密码或者账号错误")
except Exception as result:
   print(result)
   print("账号不存在")
