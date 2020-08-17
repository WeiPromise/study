#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 16:01

# 元组和列表很像，都是用来保存多个数据
# 使用一对小括号() 来表示一个元组
# 元组和列表的区别在于，列表是可变的，而元组是不可变的

words = ['hello', 'word']
nums = (1, 2, 3, 4, 5, 4, 4)

words[0] = 'haahaha'

#  'tuple' object does not support item assignment,元组不可变
# nums[2] = 2

# 统计一个元素出现的次数
print(nums.count(4))
# 获取一个元素第一次出现的索引
print(nums.index(4))

# 特殊情况
# 一个元素的元组
ages = (18,)

# 可迭代对象转换到元组
word = tuple(words)

# 元组之间支持加法运算+

a = ('hello', 'world')
b = ('I', 'love')
c = a+b
print(c)

# 遍历

for index, num in enumerate(nums):
    print(index, num)

print(words, nums, ages, word, sep='\n')
