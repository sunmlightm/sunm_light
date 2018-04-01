import time
from multiprocessing import Pool,Manager

list=[]


def dowland(i):
	print("正在下载第"+str(i)+"张图片")
	q.put(i)
	time.sleep(1)

def print_(i):
	while True:
		try:
			pic=q.get(timeout=1)
			list.append(pic)
			num=len(list)/4*100
			print("\r下载第"+str(len(list))+"张图片成功",end="\n")
			print("\r当前下载进度:%d%%"%num,end="")
			time.sleep(0.5)
		except:
			break


if __name__ == '__main__':
	q=Manager().Queue()
	p=Pool()
	for i in range(1,5):
		p.apply_async(dowland,args=(i,),callback=print_)
	p.close()
	p.join()

