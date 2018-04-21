import MysqlHelper,re
import hashlib


helper = MysqlHelper.MysqlHelper(host='192.168.153.134')

name = input("请输入你注册的账号:")
password = input("请输入你的密码:")
result=re.match("\w{4,20}",password)
if result==None:
    print("请输入4~10位的密码")
else:
    password = hashlib.sha1(password.encode("utf-8")).hexdigest()
    print(password)

    sql = 'insert into userinfos(id,uname,upwd,isDelete) values(0,%s,%s,0)'

    params = [name,password]

    result=helper.change(sql,params)

    if result == None:
       print("注册失败..")
    else:
       print("注册成功..")



