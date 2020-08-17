#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 17:47

nums = [2, 3, 15, 34, 43, 7, 5, 9]

for index, num in enumerate(nums):
    print(num, index)

num01 = nums  # 两个共享同一块内存，相互影响

print('nums={},nums01={}'.format(id(nums), id(num01)))

# copy :可以复制一个列表，和原有列表内容一样，但指向地址不一样
x = nums.copy()
print('nums={},x={}'.format(id(nums), id(x)))

# 还可以使用copy模块实现拷贝
import copy

a = copy.copy(nums)  # 等价于x.copy,都是浅克隆
print('nums={},a={}'.format(id(nums), id(a)))

print(a)

# 切片其实就是一个浅拷贝
b = nums[1:]
print('nums={},b={}'.format(id(nums), id(b)))
