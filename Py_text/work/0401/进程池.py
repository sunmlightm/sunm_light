from multiprocessing import Pool
from time import sleep
import os

# 创建进程任务函数
def test(num):
	print("text%d,子进程ID:%d,父进程ID:%d"%(num,os.getpid(),os.getppid()))
	sleep(0.5)

pool=Pool(3)
for i in range(10):
	pool.apply_async(test,args=(i,))
pool.close()
pool.join()

