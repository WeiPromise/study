#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/19 22:07

import threading,time

def dance():
    for i in range(50):
        time.sleep(0.2)
        print('我正在跳舞')


def singe():
    for i in range(50):
        time.sleep(0.2)
        print('我正在唱歌')


# 多个任务同来执行
# Python里执行多任务：多线程，多进程，多线程+多线程
# dance()
# singe()

# target 需要的事一个函数，用来指定线程需要执行的任务
t1 = threading.Thread(target=dance)
t2 = threading.Thread(target=singe)

t1.start()
t2.start()