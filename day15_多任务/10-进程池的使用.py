#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/20 22:23

from multiprocessing import Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print('{}开始执行，进程号为{}'.format(msg,os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()

    print(msg,'执行完毕，耗时%0.2f' % (t_stop - t_start))


if __name__ == '__main__':

    # 定义一个进程池，最大进程数为3
    po =Pool(3)

    for i in range(0,10):
        # Pool().apply_async(要调用的目标，(传递给目标的参数元组))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker,(i,))

    print('----start------')
    po.close() # 关闭进程池，关闭后po不在接收新的请求
    po.join() # 等候po中所有子进程执行完成，必须放在close语句之后
    print('----end------')