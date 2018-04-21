import MysqlHelper

helper=MysqlHelper.MysqlHelper(host='192.168.153.134',user='sunml',password=1122,db='python2')

sql="""
create table userinfos(
id int primary key auto_increment,
uname varchar(20) unique,
upwd varchar(40),
isdelete bit default 0
)charset=utf8;

"""
helper.change(sql)