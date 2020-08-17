#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 15:49
import copy

# 浅复制（拷贝）

nums = [1, 2, 3, 4, 5]

nums1 = nums  # 这是赋值，不是赋值

# 浅复制，内容一样，对象不一样（地址不一样）
nums2 = nums.copy()
nums3 = copy.copy(nums)

print('nums={},nums2={}'.format(id(nums), id(nums2)))
print('nums={},nums3={}'.format(id(nums), id(nums3)))

# 深复制，只能采用copy模块实现
words = ['hello', 'good', [1, 2, 4], 'yes']

words1 = copy.copy(words)  # 浅复制

words2 = copy.deepcopy(words)  # 深复制

words[0] = 'hello01'
words[2][1] = 7
print(words, words1, words2, sep='\n')

print('words={},words1={}'.format(id(words), id(words1)))
print('words={},words2={}'.format(id(words), id(words2)))
