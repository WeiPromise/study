#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/15 16:02

import time


def cal_time(fn):
    start = time.time()  # 获取当前时间的时间戳
    print('start : {}'.format(start))
    result = fn()
    end = time.time()  # 获取当前时间的时间戳
    print('end : {}'.format(end))
    cost = end - start
    print('cost : {}'.format(cost))

    return result



def demo1():
    x = 0
    for i in range(1, 100000000):
        x += i
    return x

def demo2():
    print('hahaha')
    time.sleep(3)
    print('heheheh')
    return 'leiwei'

print(cal_time(demo1))
print(cal_time(demo2))






