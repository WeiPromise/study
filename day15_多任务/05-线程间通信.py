#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/20 17:32

import threading,time
import queue

def produce():
    for i in range(100):
        time.sleep(2)
        print('生产了面包{}{}'.format(threading.current_thread().name,i))
        q.put('{}'.format(i))

def consumer():
   while True:
        time.sleep(4)
        print('买了面包:{}{}'.format(threading.current_thread().name,q.get()))


# 创建队列
# q是一个阻塞队里，q.get()是一个阻塞方法，它会一直等
# 先进先出
q = queue.Queue()

p1 = threading.Thread(target=produce,name='pa')
p2 = threading.Thread(target=produce,name='pb')
p3 = threading.Thread(target=produce,name='pc')
c4 = threading.Thread(target=consumer,name='cd')
c1 = threading.Thread(target=consumer,name='ca')
c2 = threading.Thread(target=consumer,name='cb')
c3= threading.Thread(target=consumer,name='cc')


p1.start()
p2.start()
p3.start()
c1.start()
c2.start()
c3.start()
c4.start()

