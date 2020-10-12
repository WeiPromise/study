#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/9 16:48


class Fibonacci(object):
    def __init__(self,n):
        self.n = n
        self.num1 = self.num2 = 1
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.n:
            self.index+=1
            x = self.num1
            self.num1,self.num2 = self.num2,self.num1+self.num2
            return x
        else:
            raise StopIteration



f = Fibonacci(12) # 占时间，不占用空间

for i in f:
    print(i)



# 既然有列表了，为什么还要有生成器呢？
# 列表占空间，不占时间

