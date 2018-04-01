import os
import time
from multiprocessing import Pool

#1.原文件夹
old_dir_name=input("请输入源文件夹的名称：")

#２.目标文件夹
new_dir_name=old_dir_name+"_复制"
result=os.mkdir(new_dir_name)


#遍历文件夹里所有文件
file_list=os.listdir(old_dir_name)


#定义进程的任务
def copy_file():
	fr=None
	fw=None
	try:
		for file in file_list:
			fr=open(old_dir_name+"/"+file,"r")
			print(fr)
			fw=open(new_dir_name+"/"+file,"w")

			#开始读写
			all=fr.read()
			fw.write(all)

	except Exception as result:
		print("复制失败",result)


	finally:
		if fr!=None:
			fr.close()
		if fw!=None:
			fw.close()

		print("复制完成")

def look_progress(queue):
	try:
		i=0
		while True:
			filename=queue.get(timeout=2)
			i+=1
			print("\r复制文件的进度：%d%%"%(i/len(file_list)*100),end="")
	except Exception as result:
		print("文件读取完毕",result)

start_=time.time()
if __name__=="__main__":
	pool=Pool()
	pool.apply_async(copy_file)
	pool.close()
	pool.join()
end_=time.time()
print(end_-start_)
