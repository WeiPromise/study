#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/21 11:13


import socket

# 基于TCP的scoket连接

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('192.168.10.179',9090))
server_socket.listen(128)

# data的数据类型是一个元组
# 第0个元素是接受的数据
# 第1个元素是发送方的ip地址和端口

client_socket,client_addr= server_socket.accept()

# 从客户端的socket里获取数据
data = client_socket.recv(1024).decode('utf8')
print(data)

# 在返回内容之前，需要先设置HTTP响应头,设置一个响应头就换一行
client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
client_socket.send('content-type:text/html\n'.encode('utf8'))

# 设置完所有响应头后，再换一行
client_socket.send('\n'.encode('utf8'))

# 给客户端返回消息
client_socket.send('hello world'.encode('utf8'))

