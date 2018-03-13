file_name=input("请输入要复制的文件名")
file_old=open(file_name,"r")
position=file_name.rfind(".")
file_a=file_name[:position]
file_b=file_name[position:]
file_c=file_a+"[副本]"+file_b
file_new=open(file_c,"w")

value=file_old.read(1024)
while len(value)!=0:
    file_new.write(value)
    value = file_old.read(1024)
file_old.close()
file_new.close()