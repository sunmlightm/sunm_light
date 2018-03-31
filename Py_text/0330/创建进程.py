
import os
import time
# 创建子进程
pid=os.fork()
if pid==0:
    for i in range(10):
        print(i)
        time.sleep(0.5)
# 执行主进程
elif pid>0:
    for i in range(10):
        print("a")
        print("b")
        time.sleep(0.5)