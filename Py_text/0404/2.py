from socket import *

'''
1. 准备服务端IP地址和端口号
2. 创建socket套接字
3. 使用套接字与IP和端口号建立连接
4. 进行通信
5. 关闭
'''
# 1. 准备服务端IP地址和端口号
ip = "192.168.21.40"
port = 8899
send_address = (ip, port)

# 2.创建socket套接字
client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.bind(("", 8889))

# 3.使用套接字与IP和端口号建立连接
test = client_socket.connect(send_address)  # 此时底层会进行三次握手
print("客户端:", test)

# 4.关闭
client_socket.close()
