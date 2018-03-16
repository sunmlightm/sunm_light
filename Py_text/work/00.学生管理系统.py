#1.添加用户  ----》磁盘中 ----》users.txt ----》一个用户一行 ----->str=张三 18 男 北京
													  # ------>{"name":"张三",...}
#2.查询用户  ---->读取users.txt中的数据  ----->每读取一行就是一个用户信息

#3.修改学生信息  选择修改哪一项：  姓名 年龄 性别 地址

#4.删除学生信息  ？？？？ 


#添加学生信息
def add_student():
	#结合文件
	stream=open("users.txt","a")
	#使用stream进行写操作
	stream.write(input("输入姓名:"))
	stream.write(" "+input("输入年龄:"))
	stream.write(" "+input("输入性别:"))
	stream.write(" "+input("输入地址:"))
	stream.write("\n")
	#关闭流
	stream.close()

	print("添加新用户成功！")

#查询学生信息
def search_student():
	print("所有的学生信息如下:")
	#查询文件
	stream=open("users.txt","r")
	#安照行读取内容
	while True:
		line=stream.readline()
		print(line)
		if len(line)==0:
			break
	#关闭流
	stream.close()


#修改学生信息
"""
思路：
1.通过循环，每次读取一行信息 
2.每读取一行信息判断是否有要更新的内容
3.如果发现则可以使用替换replace，替换成新的信息，将新内容写入文件
4.如果没有发现则将当前行写入文件

注意L其实就是使用的是：读取内容---查找---写内容（写的内容是覆盖原来的内容，包括没有发现的行也是一模一样的覆盖原来内容）
"""
def update_student():
	pass



#删除学生信息
"""
1.通过循环，每次读取一行信息
2.判断改行中有没有要删除的学生信息可以使用search方法查找
3.如果发现则不写入，没有发现的继续写入文件即可

"""
def delete_student():
	pass


#定义学生管理系统
def system_manager():

	while True:
		print("="*50)
		print("1.添加学生信息")
		print("2.查询学生信息")
		print("3.修改学生信息")
		print("4.删除学生信息")
		print("5.退出系统")
		print("="*50)
		choice=input("请输入您的选择:")

		#判断选择
		if int(choice)==1:
			#添加学生信息
			add_student()

		elif int(choice)==2:
			#查询学生信息
			search_student()
		elif int(choice)==3:
			#修改学生信息
			update_student()

		elif int(choice)==4:
			#删除学生信息
			delete_student()

		elif int(choice)==5:
			#退出系统
			print("即将退出系统....")
			break






#调用系统
system_manager()