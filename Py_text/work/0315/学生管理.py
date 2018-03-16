def add_st():
    stream=open("user.txt","a")
    stream.write(input("请输入姓名:"))
    stream.write(" "+input("请输入年龄:"))
    stream.write(" "+input("请输入性别:"))
    stream.write(" "+input("请输入地址:"))
    stream.write("\n")

def search_st():
    print("所有学生信息如下:")
    stream=open("user.txt","r")
    while True:
        line=stream.readline()
        print(line)
        if len(line)==0:
            break

def update_st():
    name=input("请输入要修改的姓名")
    stream=open("user.txt","r")
    lines=stream.readlines()
    stream.close()
    for str in lines:
        if str.find(name)!=-1:
            lines.remove(str)
            age = input("请输入要修改的年龄")
            sex = input("请输入要修改的性别")
            address = input("请输入要修改的地址")
            str_new=name+" "+age+" "+sex+" "+address
            lines.append(str_new)
            break
    str_sts="\n".join(lines)
    stream = open("user.txt", "w")
    stream.write(str_sts)
    stream.close()
def delete_st():
    name=input("请输入一个姓名")
    stream = open("user.txt", "r")
    lines = stream.readlines()
    stream.close()
    for str in lines:
        if str.find(name) != -1:
            lines.remove(str)
            break
    str="\n".join(lines)
    stream = open("user.txt", "w")
    stream.write(str)
    stream.close()

def system_manager():
    while True:
        print("="*50)
        print("\t1.添加学生信息")
        print("\t2.查询学生信息")
        print("\t3.修改学生信息")
        print("\t4.删除学生信息")
        print("\t5.退出")
        print("="*50)
        choice=int(input("请输入您的选择:"))

        if choice==1:
            add_st()
        elif choice==2:
            search_st()
        elif choice==3:
            update_st()
        elif choice==4:
            delete_st()
        elif choice==5:
            print("即将退出系统...")
            break

system_manager()