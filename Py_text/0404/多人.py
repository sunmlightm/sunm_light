from socket import *

# 1. 服务端IP地址和端口号
from threading import Thread

ip = "192.168.21.40"
port = 8890

# 2. 服务器端也是一个套接字socket
server_socket = socket(AF_INET, SOCK_STREAM)

# 3. 绑定IP和端口号
server_socket.bind((ip, port))

# 4.设置socket监听listener
server_socket.listen(3)

print("=====>服务器准备好了，等待客户端的连接")

# 服务端的所有的socket列表
user_list = []


def qunfa(user_list, socket):
    # 接收自己的信息
    msg = socket.recv(1024)
    # 遍历列表给别人发信息
    for user in user_list:
        user[0].sendto(msg.decode("utf-8"), user[1])


while True:
    new_client = server_socket.accept()  # new_client=(new_socket,new_address)
    user_list.append(new_client)

    Thread(target=qunfa, args=(user_list, new_client[0]))

server_socket.close()
