#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 15:40

# 列表推导式作用是使用简单的语法创建一个列表

nums = [i for i in range(10)]
print(nums)

x = [i for i in range(10) if i % 2]

print(x)

# points 是一个列表，这个列表的元素都是元组
points = [(x, y) for x in range(5, 10) for y in range(10, 15)]

# print(points)

m = [i for i in range(1, 101)]

n = [m[j:j + 3] for j in range(0, 100, 3)]

print(n)
