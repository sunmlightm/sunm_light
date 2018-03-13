# 定义一个初始学生信息表
list_info=[{"name":"zhang","age":"20","address":"Hebei"},{"name":"wang","age":"22","address":"Beijing"}]
# 定义主函数
def main():
    # 打印操作指南
    print("=" * 50)
    print("\t >>学生信息管理系统<<")
    print("\t1.新建学生信息")
    print("\t2.删除学生信息")
    print("\t3.修改学生信息")
    print("\t4.查询学生信息")
    print("\t5.退出学生信息管理系统")
    print("=" * 50)
    # 循环执行
    while True:
        # 输入操作指令执行对应的函数
        num = int(input("请输入您的选项："))
        if num==1:
            list_add()
        elif num==2:
            list_remove()
        elif num==3:
            list_update()
        elif num==4:
            list_search()
        elif num==5:
            break
        else:
            print(">>请输入正确的选项!!!")

# 定义学生信息添加函数
# 新建一个空字典
# 依次向空字典输入添加姓名，年龄，住址
# 将添加信息之后的字典添加进信息列表
# 打印信息列表
def list_add():
    st_add = {}
    st_add["name"] = input("请输入姓名：")
    st_add["age"] = input("请输入年龄：")
    st_add["address"] = input("请输入住址：")
    list_info.append(st_add)
    print(list_info)
# 定义学生信息移除函数
# 输入要删除的姓名
# 定义标志位
# 循环遍历学生信息找到输入的学生的字典
# 删除此字典并打印学生信息表，改变标志位
# 若标志位未改变则打印"sorry，没有搜索到此名"
def list_remove():
    name_re=input("请输入要删除的学生姓名")
    flg = 0
    for st_re in list_info:
        if name_re == st_re['name']:
            list_info.remove(st_re)
            print(list_info)
            flg = 1
    if flg == 0: print("sorry，没有搜索到此名")
# 定义学生信息更新函数
# 输入要修改的学生姓名
#　循环遍历学生信息找到要修改的学生字典
# 输入新的学生信息
# 打印学生信息表，改变标志位
def list_update():
    name_re = input("请输入要修改的学生姓名")
    flg = 0
    for st_update in list_info:
        if name_re == st_update['name']:
            st_update["name"] = input("请输入修改后的姓名：")
            st_update["age"] = input("请输入修改后的年龄：")
            st_update["address"] = input("请输入修改后的住址：")
            print(list_info)
            flg = 1
    if flg == 0: print("sorry，没有搜索到此名")
# 定义学生信息查找函数
# 输入要查找的学生姓名
#　循环遍历学生信息找到要查找的学生字典
# 打印学生信息，改变标志位
# 若标志位被改变则打印"sorry，没有搜索到此名"
def list_search():
    name_se = input("请输入要查找的学生姓名")
    flg = 0
    for st_se in list_info:
        if name_se==st_se['name']:
            print("您要查找的学生信息是：",st_se)
            flg = 1
    if flg == 0: print("sorry，没有搜索到此名")

main()

