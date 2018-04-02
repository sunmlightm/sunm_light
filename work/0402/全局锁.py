import threading,time
lock=threading.local()

def print_():
	str=lock.str
	print(str)

def str_(str):
	for i in  str:
		lock.str=i
		print_()
		time.sleep(0.5)

list_a=[x for x in range(65,91)]
list_num=[x for x in range(1,27)]
list2=[]
for i in list_a:
	list2.append(chr(i))
t1=threading.Thread(target=str_,args=(list2,))
t2=threading.Thread(target=str_,args=(list_num,))
t1.start()
t2.start()
t1.join()


