#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/9 16:04

# 有很多可迭代对象：list/tuple/dict/set/str/range/filter/map
# for ... in 可迭代对象

from collections import Iterable


class Demo(object):

    def __init__(self,x):
        self.x = x
        self.count = 0

    # 写了这个方法，他就是可迭代对象
    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.x:
            self.count += 1
            return self.count-1
        else:
            raise StopIteration #停止



d = Demo(10)

print(isinstance(d,Iterable))


# for...in循环的本质就是调用可迭代对象__iter__方法，获取到这个方法的返回值
# 这个返回值是一个对象，然后再调用这个对象的__next__方法
for x in d:
    print(x)
