#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 17:22

nums = [2, 3, 15, 34, 43, 7, 5, 9]

a = 12
b = a
print('修改前，a={},b={}'.format(id(a), id(b)))
a = 10
print('修改后，a={},b={}'.format(id(a), id(b)))
print(b)  # 12

nums01 = nums
# nums01 = list(nums)  # 这种方法是开辟一块新的内存空间

print('修改前，nums={},nums01={}'.format(id(nums), id(nums01)))
nums[2] = 17
print('修改后，nums={},nums01={}'.format(id(nums), id(nums01)))
print(nums01)
