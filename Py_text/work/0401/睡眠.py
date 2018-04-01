from threading import Thread
from time import sleep
import random

def text1():
	i=0
	while i<200:
		for x in range(10):
			print("线程1:",x)
			i+=1
		sleep(0.5)

def text2():
	i = 0
	while i < 200:
		for x in range(20):
			print("线程2:",x)
			i += 1
		sleep(0.5)

if __name__ == '__main__':
	t1=Thread(target=text1)
	t2=Thread(target=text2)
	t1.start()
	t2.start()
	t1.join()
	t2.join()