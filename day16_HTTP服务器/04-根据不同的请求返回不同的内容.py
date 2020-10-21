#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/21 15:08

"""
GET /favicon.ico HTTP/1.1
Host: localhost:9090
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: image
Referer: http://localhost:9090/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: Webstorm-afeacc=6fce94e3-79ce-4bf5-90bc-b4d17a1fc3ff
"""


import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0',9090))
server_socket.listen(128)

while True:
    client_socket, client_addr = server_socket.accept()

    # 从客户端的socket里获取数据
    data = client_socket.recv(1024).decode('utf8')
    path = data.splitlines()[0].split(' ')[1]

    response_header_host = 'HTTP/1.1 200 OK\n'


    response_body = 'hello world'
    if path == '/login':
        response_body = '欢迎来到登录页'
    elif path == '/register':
        response_body = '欢迎来到注册页'
    elif path == '/':
        response_body = '欢迎来到首页'
    else:
        response_body = '你要查找的页面不存在'
        response_header_host = 'HTTP/1.1 404 Page Not Found\n'

    response_header = response_header_host+'content-type:text/html;charset=UTF-8\n\n'
    response = response_header+response_body
    client_socket.send(response.encode('utf8'))
