#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/15 16:43

import time

def cal_time(fn):
    print('我是外部函数，我被调用了！！！')
    print('fn = {}'.format(fn))
    def inner(x,*args,**kwargs):
        start = time.time()  # 获取当前时间的时间戳
        print('start : {}'.format(start))
        result=fn(x) # 这边参数给不了可变的
        end = time.time()  # 获取当前时间的时间戳
        print('end : {}'.format(end))
        cost = end - start
        print('cost : {}'.format(cost))
        return result
    return inner


@cal_time # 第一件事调用cal_time函数；第二件事把被装饰函数传递给fn;
def demo1(n):
    x = 0
    for i in range(1, n):
        x += i
    return x

@cal_time
def demo2():
    print('hahaha')
    time.sleep(3)
    print('heheheh')


# 第三件事，当再次调用demo1函数时，现在的demo1函数已经不再是上面的demo1了，而是装饰后的inner函数
print('装饰后的demo1 : {}'.format(demo1))
print(demo1(10000000)) # 执行顺序：inner->demo1->返回值在inner里要返回才会有

# demo2()