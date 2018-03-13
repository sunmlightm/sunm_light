file_old=input("请输入要修改的文件名")
file_new=input("请输入正确的的文件名")
import os
os.rename(file_old,file_new)