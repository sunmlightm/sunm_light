print('='*50)
print('   名片管理')
print('   1.增加一个新名片')
print('   2.删除')
print('   3.修改')
print('   4.查找')
print('='*50)
names=[]
while True:
    num=int(input('输入编号'))
    if num==1:
        new_name=input('输入新名片名称')
        names.append(new_name)
        print(names)
    elif num==2:
        remove_name=input('输入要删除的名称')
        names.remove(remove_name)
        print(names)
    elif num==3:
        before_name=input('需要修改的名称')
        now_name=input('想要修改成什么？')
        be_index=names.index(before_name)
        names[be_index]=now_name
        print(names)
    elif num ==4:
        pass
    else:
        print('请输入正确的数字')