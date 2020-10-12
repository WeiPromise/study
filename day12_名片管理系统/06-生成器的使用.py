#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/10 18:53

# 生成器本质也是一个迭代器，它是一个特殊的迭代器

# 最简单的生成器
# nums = [i for i in range(10)]  #列表生成式（推导式）
# print(nums)
#
#
#
# g = (i for i in range(10)) # 得到的结果是生成器
#
# for m in g: # 生成器是一个特殊的迭代器，也可以方法在for...in后面
#     print(m)


# 迭代器是一个对象，定义class
# 生成器写法上像一个函数

def m_gen(n):
    i = 0
    while i < n:
        # return i # 函数结束
        yield i  # yield 关键字，将函数变成生成器
        i += 1


G = m_gen(10)


# print(G) #<generator object m_gen at 0x0000022B1EFA79E8>

# for i in G:
#     print(i)


def fibonacci(n):
    num1 = num2 = 1
    count = 0
    while count <= n - 1:
        x = num1
        num1, num2 = num2, num2 + num1
        count += 1
        yield x


f = fibonacci(12)

for i in f:
    print(i)
