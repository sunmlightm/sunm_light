dict_list=[{"name":"wukong","wechat":"wukong_123"}]
print("1.add")
print("2.del")
num=int(input("please enter your num"))
if num==1:
    name=input("please ")
elif num==2:
    name=input("please enter one name")
    flg=0
    for dict_item in dict_list:
        if name==dict_item.get("name"):
            dict_list.remove(dict_item)
            print(dict_list)
            flg=1
    if flg==0:
        print("can not find the name")
elif num==3:
    pass

