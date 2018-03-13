# 新建本地文件ｗｏｒｋ＃
# 写入内容
# 关闭
f_open=open("work#","w")
f_open.write("1.此行没有＃\n２.此行没有＃\n#３.此行有＃\n４.此行没有＃\n#５.此行有＃")
f_open.close()
# 打开文件
# 获取所有行存在ｌｉｓｔ中
# 遍历ｌｉｓｔ
# 取出每行的第一个字母与＃相比较
# 若第一个字母不是＃则打印这一行
# 关闭文件
f=open("work#","r")
list=f.readlines()
for line in list:
    first=line[:1]
    if first!="#":
        print(line)
f.close()