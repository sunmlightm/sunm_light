# 使用multiprocessing创建进程
from multiprocessing import Process
from time import sleep
import os
# 定义子进程
def test():
    for i in range(10):
        print("子进程===>子进程ID:%d,父进程ID:%d"%(os.getpid(),os.getppid()))
        sleep(1)

if __name__ == "__main__":
    # 创建子进程
    p = Process(target=test)
    # 开始运行子进程
    p.start()
    # 创建主进程
    for i in range(10):
        print("父进程===>子进程ID:%d,父进程ID:%d"%(os.getpid(),os.getppid()))
        sleep(1)
