#encoding=utf-8
# @Time    : 4/21/18 9:33 PM
# @Author  : sunml
from socket import *

def handler_client(client_socket):
    # 就是客户端（浏览器给我们发送的请求）
    request = client_socket.recv(1024)
    print(request)

    #就是服务器给浏览器返回的相应信息 response
    client_socket.send(b'HTTP/1.1 200 OK \r\n\r\n')
    client_socket.send(b'i love you!')

def main():
    #创建socket 就是买来一部手机
    myscoket = socket(AF_INET,SOCK_STREAM)
    #给手机办卡
    myscoket.bind(('',8080))
    #设置手机最大监听数
    myscoket.listen(5)
    while True:
        #等待链接，等人给打电话
        client_socket,client_info = myscoket.accept()
        handler_client(client_socket)
        client_socket.close()

#只有当此脚本文件执行的时候，才会调用main函数，如果作为模块去引用，main函数不执行
if __name__ == '__main__':
    main()