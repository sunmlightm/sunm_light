from socket import *

udp_sokect = socket(AF_INET, SOCK_DGRAM)
send_address = "172.23.169.17"

udp_sokect.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    send_content = input("请你输入要发送的内容:")
    send_content = "1:12312312312:meinv:mm-pc:32:%s" % send_content
    udp_sokect.sendto(send_content.encode("gb2312"), (send_address, 2425))

udp_sokect.close()
