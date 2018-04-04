from socket import *

'''
1. 服务端IP地址和端口号  ----》客户端
2. 服务器端也是一个套接字socket   
        UDP   socket(AF_INET,SOCK_DGRAM)
        TCP   socket(AF_INET,SOCK_STREAM)
3. 绑定IP和端口号
4. 设置socket监听listener 
5. accept() 同意   ---》连接
6. 接收或者发送数据
7. 关闭
'''
# 1. 服务端IP地址和端口号
ip = "192.168.21.40"
port = 8899

# 2. 服务器端也是一个套接字socket
server_socket = socket(AF_INET, SOCK_STREAM)

# 3. 绑定IP和端口号
server_socket.bind((ip, port))

# 4.设置socket监听listener
server_socket.listen(3)

print("=====>服务器准备好了，等待客户端的连接")
# 5. accept() 同意
new_socket, new_address = server_socket.accept()  # 阻塞式的方法  有客户端连接的时候才会不会阻塞

print("new_socket:", new_socket)
print("new_address", new_address)

# 6.关闭
new_socket.close()
server_socket.close()
