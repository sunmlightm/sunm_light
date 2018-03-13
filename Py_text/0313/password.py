import os
def main():
    print("=" * 50)
    print("\t >>密码薄<<")
    print("\t1.新建密码")
    print("\t2.删除密码")
    print("\t3.修改密码")
    print("\t4.查询密码")
    print("\t5.退出密码薄")
    print("=" * 50)
    # 循环执行
    list_info = search()
    while True:
        # 输入操作指令执行对应的函数
        num = int(input("请输入您的选项："))
        if num == 1:
            list_add(list_info)
        elif num == 2:
            list_remove(list_info)
        elif num == 3:
            list_update(list_info)
        elif num == 4:
            list_search(list_info)
        elif num == 5:
            break
        else:
            print(">>请输入正确的选项!!!")

def search():
    password_l = [{"address":"www.atguigu.com","password":"123456"}]
    file_lists=os.listdir("./")
    flg=0
    for file in file_lists:
        if file=="pass_word.txt":
            f=open("pass_word.txt","r")
            list_infos=f.read()
            f.close()
            list_info=eval(list_infos)
            flg=1
            return list_info
    # 若标志位未改变（表示本地没有此文件）
    # 调用file_input函数新建本地数据文件
    # 给list_info并ｒｅｔｕｒｎ
    if flg==0:
        file_input(str(password_l))
        list_info=password_l
        return list_info
def file_input(st_list):
    f=open("pass_word.txt","w")
    f.write(st_list)
    f.close()

def list_add(list_info):
    st_add = {}
    st_add["address"] = input("请输入网址：")
    st_add["password"] = input("请输入密码：")
    list_info.append(st_add)
    file_input(str(list_info))

def list_remove(list_info):
    address=input("请输入要删除的网址")
    flg = 0
    for st_re in list_info:
        if address == st_re['address']:
            list_info.remove(st_re)
            file_input(str(list_info))
            flg = 1
    if flg == 0: print("sorry，没有搜索到这个网址")

def list_update(list_info):
    address = input("请输入要修改密码的网址")
    flg = 0
    for st_update in list_info:
        if address == st_update['address']:
            st_update["password"] = input("请输入修改后的密码：")
            file_input(str(list_info))
            flg = 1
    if flg == 0: print("sorry，没有搜索到这个网址")

def list_search(list_info):
    name_se = input("请输入要查找的网址")
    flg = 0
    for st_se in list_info:
        if name_se==st_se['address']:
            print("您要查找的密码是：",st_se)
            flg = 1
    if flg == 0: print("sorry，没有搜索到这个网址")

main()