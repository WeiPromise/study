#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/20 18:11

import multiprocessing
import time,os


def dance(num):

    for i in range(num):
        time.sleep(1)
        print('{}正在跳舞'.format(os.getpid()))


def singe(num):
    for i in range(num):
        time.sleep(1)
        print('{}我正在唱歌'.format(os.getpid()))



# win系统下，只能在执行python文件的时候才会开启进程
if __name__ == '__main__':

    p1 = multiprocessing.Process(target=dance,args=(100,))
    p2 = multiprocessing.Process(target=singe,kwargs={'num':100})

    p1.start()
    p2.start()
