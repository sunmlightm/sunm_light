def dic(dic_info):
    for it in dic_info.items():
        print(it)
def dic_up(dic_info):
    dic(dic_info)
    key=input("请输入要修改的项")
    value=input("请输入要修改的内容")
    dic_info[key]=value
    dic(dic_info)
dic_up({"name":"wukong","age":"18"})