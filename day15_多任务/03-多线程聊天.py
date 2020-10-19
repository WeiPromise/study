#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/19 22:41
import threading,time

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = '192.168.3.69'
s.bind((port,9090))

def send_msg():
    while True:
        msg = input()
        if msg == 'exit':
            break
        s.sendto(msg.encode('utf-8'),('192.168.3.69',8080))
        print('{}:{}-{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'), port, msg))

# data的数据类型是一个元组
# 第0个元素是接受的数据
# 第1个元素是发送方的ip地址和端口
def recv_msg():
    while True:
        data,addr = s.recvfrom(1024)
        print('{}:{}-{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'),addr[1],data.decode('utf8')))

t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)

t1.start()
t2.start()