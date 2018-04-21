import MysqlHelper

helper=MysqlHelper.MysqlHelper(host='192.168.153.134',user='sunml',password=1122,db='python2')
# 查找
helper.get_all('select * from students',prams=[])
# 增加一条数据
helper.change("insert into students(id,name) values(%s,%s)",['0','jack'])
# 删除
helper.change("delete from students where name=%s",['张良'])
# 更改
helper.change("update students set name = %s where name=%s",['王二','张飞'])

helper.get_all('select * from students',prams=[])