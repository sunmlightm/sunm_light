import socket
from threading import Thread

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind(("",8080))
def send_():
	while True:
		msg=input("msg:\n")
		send_address=("172.23.169.17",8080)
		udp_socket.sendto(msg.encode("gb2312"),send_address)
def recv_():
	while True:
		recv_msg=udp_socket.recvfrom(1024)
		print(recv_msg[0].decode("gb2312"))
		print("发消息请按回车键")

t1=Thread(target=send_)
t2=Thread(target=recv_)
t1.start()
t2.start()