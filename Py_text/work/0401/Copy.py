from  multiprocessing import Process

def copy_file(name):
	name_list=name.split(".")
	f=open(name,"rb")
	name_new=name_list[0]+"_副本."+name_list[1]
	f_new=open(name_new,"wb")
	while True:
		value=f.read(1024)
		f_new.write(value)
		if len(value)==0:
			break
	f.close()
	f_new.close()

if __name__ == '__main__':
	p=Process(target=copy_file,args=(input("请输入要拷贝的文件名字"),))
	p.start()
	print("创建成功")