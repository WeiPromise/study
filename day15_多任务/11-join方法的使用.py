#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/20 22:40

# join 线程和进程都有join方法
import threading

import time

x = 10

def my_test(a,b):
    time.sleep(1)
    global x
    x = a + b

# my_test(1,2)
# print(x)

t = threading.Thread(target=my_test,args=(1,4))
t.start()
t.join() # 让主线程等待执行完
print(x) # 10



