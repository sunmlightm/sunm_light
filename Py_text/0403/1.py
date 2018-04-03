import socket


udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_socket.bind(("192.168.21.32",8081))

msg=input("msg:")

send_address=("192.168.21.32",8080)
udp_socket.sendto(msg.encode("utf-8"),send_address)

while True:
	recv_msg=udp_socket.recvfrom(1024)
	print(recv_msg[0].decode("utf-8"))
	print(recv_msg[1])
