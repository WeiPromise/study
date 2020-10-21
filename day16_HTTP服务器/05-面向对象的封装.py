#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/21 15:08


import socket

class MyServer(object):

    def __init__(self,ip,port):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        self.socket.listen(128)

    def run_forever(self):
        while True:
            client_socket, client_addr = self.socket.accept()

            # 从客户端的socket里获取数据
            data = client_socket.recv(1024).decode('utf8')
            path = data.splitlines()[0].split(' ')[1]

            response_header_host = 'HTTP/1.1 200 OK\n'

            if path == '/login':
                response_body = '欢迎来到登录页'
            elif path == '/register':
                response_body = '欢迎来到注册页'
            elif path == '/':
                response_body = '欢迎来到首页'
            else:
                response_body = '你要查找的页面不存在'
                response_header_host = 'HTTP/1.1 404 Page Not Found\n'

            response_header = response_header_host + 'content-type:text/html;charset=UTF-8\n\n'
            response = response_header + response_body
            client_socket.send(response.encode('utf8'))


server = MyServer('0.0.0.0',9090)

server.run_forever()