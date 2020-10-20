#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/20 21:16


import os
import threading,multiprocessing


n = 100


def my_test():
    global n
    n += 1

    print('{}：n的值是{}'.format(os.getpid(),n))


def demo():
    global n
    n += 1

    print('{}：n的值是{}'.format(os.getpid(),n))

#同一个主进程里的两个子线程，线程之间可以共享同一个进程的全局变量
# t1 = threading.Thread(target=my_test)
# t2 = threading.Thread(target=demo)
# t1.start()
# t2.start()

if __name__ == '__main__':
    # 不同进程之间不共享全局变量，每个进程独立保留一份全局变量
    m1 = multiprocessing.Process(target=my_test)
    m2 = multiprocessing.Process(target=demo)

    m1.start()
    m2.start()