from threading import Thread,Lock
list1=["a","b","c","d","e","f"]
mutex=Lock()
num=len(list1)
i=1
j=1
def test():
    global i
    mutex_flag=mutex.acquire()
    if mutex_flag:
        while i<=num:
            print(list1[i-1])
            i+=1
            mutex.release()



def test1():
    global j
    mutex_flag1=mutex.acquire()
    if mutex_flag1:
        while j<=num:
            print(j)
            j += 1
            mutex.release()





t1=Thread(target=test)
t1.start()

t2=Thread(target=test1)
t2.start()
