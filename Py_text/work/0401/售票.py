from threading import Thread
from time import sleep
train_list=[x for x in range(30)]

def seel(name):
	list=[]
	while len(train_list):
		list.append(train_list.pop())
		sleep(0.1)
	print("商户"+str(name)+"售出了"+str(list))

if __name__ == '__main__':

	p1=Thread(target=seel,args=(1,))
	p2=Thread(target=seel,args=(2,))
	p3=Thread(target=seel,args=(3,))

	p1.start()
	p2.start()
	p3.start()

