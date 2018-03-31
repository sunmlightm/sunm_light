import os
from multiprocessing import Process
num = 1
list1=["a","b","c"]

def son():
    print("这里是子进程函数")
    print(num)
    print(list1)
    print("子进程的id：",os.getpid())
if __name__=="__main__":
    p = Process(target=son)
    p.start()
    p.join(5)
    for i in range(3):
        num += 1
        list1.append(i)
        print("这里是父进程")
        print(num)
        print(list1)
    print("父进程的id：", os.getpid())
    print("完毕")

