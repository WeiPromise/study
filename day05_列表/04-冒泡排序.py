#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 16:53

nums = [2, 3, 15, 34, 43, 7, 5, 9]

i = 0
while i < len(nums) - 1:
    j = 0
    while j < len(nums) - i - 1:
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        j += 1
    i += 1
print(nums)


# 内置函数sorted(排序)，list方法sort()排序