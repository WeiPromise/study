#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/20 22:01


import queue
from multiprocessing import Queue


# 线程间通信
q1 = queue.Queue()

# 进程间通信
q2 = Queue()

# 创建队列时，可以指定最大长度，默认值是0，表示不限
q3 = Queue(5)

q3.put('hello')
q3.put('hello1')
q3.put('hello3')
print(q3.full())
q3.put('hello2')
q3.put('hello6')

# 判断是不是满了
print(q3.full())

# 当队列数量超过数量后，程序阻塞，必须拿出一个后才回放进去
# q3.put('hello8')

# block = True 当队列满的时候就阻塞
# timeout 超时，等待多久后程序出错，单位是秒
# q3.put('hello9', block=True, timeout=3)
#
# q3.put_nowait('hello123') # 等价于q3.put('hello9',block=False）

print(q3.get())
print(q3.get())
print(q3.get())
print(q3.get())
print(q3.get())

# block = True 当队列满的时候就阻塞
# timeout 超时，等待多久后程序出错，单位是秒
# q3.get(block=True,timeout=3)
q3.get_nowait()  # q3.get(block=False)





