import os
import time

# 创建子进程
pid=os.fork()
# 执行子进程
print("pid:",pid)
if pid==0:
	for i in range(5):
		print("子进程===>子进程ID:%d,父进程ID:%d"%(os.getpid(),os.getppid()))
		time.sleep(0.5)
else:
	for i in range(5):
		print("父进程===>子进程ID:%d,父进程ID:%d"%(os.getpid(),os.getppid()))
		time.sleep(0.5)

