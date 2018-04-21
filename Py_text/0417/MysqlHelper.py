import pymysql

# 创建MysqlHelper类
class MysqlHelper(object):
    # 创建初始化参数
    def __init__(self,host):
        self.host=host
        self.prot=3306
        self.user='sunml'
        self.password="1122"
        self.db='python2'
        self.charset='utf8'

    # 打开数据库链接返回connect对象-conn
    def open(self):
        self.conn=pymysql.connect(
            host=self.host,
            port=self.prot,
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8'
        )
        # 得到cursor对象
        self.cursor=self.conn.cursor()

    # 关闭链接
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 修改提交数据
    def change(self, sql, parms=[]):
        try:
            self.open()
            self.cursor.execute(sql,parms)
            result=self.cursor.fetchone()
            self.conn.commit()
            self.close()
            return "注册成功"
        except Exception as result:
            print(result)
    def get_all(self,sql,prams=[]):
        try:
            self.open()
            self.cursor.execute(sql, prams)
            result = self.cursor.fetchall()
            self.close()
            for i in result:
                print(i)
        except Exception as result:
            print(result)

    def get_one(self,sql,prams=[]):
        try:
            self.open()
            self.cursor.execute(sql,prams)
            result=self.cursor.fetchone()
            self.close()
            return result
        except Exception as result:
            print(result)






