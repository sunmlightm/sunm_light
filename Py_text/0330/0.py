try:
    # 打开文件读取全部行
    f = open("text.txt", "r")
    lists = f.readlines()
    # 定义空列表和字典备用
    lis_dic = []

    # 循环文件内容列表,以" "分割为字符串
    for st1 in lists:
        dic = {}
        lis = st1.split()
        # 将内容放进字典
        dic["name"] = lis[0]
        dic["age"] = lis[1]
        dic["sex"] = lis[2]
        # 将字典放入列表
        lis_dic.append(dic)
    print(lis_dic)
    f.close()

# 文件不存在则执行:
except FileNotFoundError:

    print("文件不存在")
except:
    f.close()
    print("其他错误")
finally:

    print("执行完毕")

