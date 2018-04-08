from threading import Thread
from socket import *

# 接收信息
def recv_data():
    while True:
        recvInfo = udp_socket.recvfrom(1024)

        print(">>：%s:%s" % (str(recvInfo[1]), recvInfo[0].decode("gb2312")))
        print("<<：")

# 2. 发送信息
def send_data():
    while True:
        sendInfo = input("<<：")
        udp_socket.sendto(sendInfo.encode("gb2312"), ("172.23.169.17", 8080))

def main():
    global udp_socket
    global target_ip
    global target_port

    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("", 8809))

    tr = Thread(target=recv_data)
    ts = Thread(target=send_data)

    tr.start()
    ts.start()

    tr.join()
    ts.join()


if __name__ == "__main__":
    main()
