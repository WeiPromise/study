#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/9 16:24

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

# print(d.__iter__().__next__())
# 内置函数iter可以获取到一个可迭代对象的迭代器
i = iter(d)