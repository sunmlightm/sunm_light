from threading import Thread,Lock
from time import sleep
#  创建两把锁,lock2先锁住
lock1=Lock()
lock2=Lock()
lock2.acquire()
# 创建字母和数字的列表各一个
list_a=[x for x in range(65,91)]
list_num=[x for x in range(1,27)]

# 定义方法1
def text1():
	flg=0
	while True:
		try:
			# 为1上锁,若上锁成功则执行打印
			if lock1.acquire():
				print(chr(list_a[flg]))
				flg+=1
				# 为lock2解锁
				lock2.release()
		except:break
def text2():
	flg=0
	while True:
		try:
			if lock2.acquire():
				print(list_num[flg])
				flg+=1
				lock1.release()
		except:break

# 创建两个线程并执行
t1=Thread(target=text1)
t2=Thread(target=text2)
t1.start()
t2.start()