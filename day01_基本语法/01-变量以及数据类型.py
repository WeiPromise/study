#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/12 17:47


a = '你好 ，世界'

print(a)

b = 34

print(b)

c = True
print(c)

# 数据类型的概念：python里数据都有各自对应的类型
# 数字：long类型在python3中已废弃
print(45)  # int 整数类型
print(3.1415)  # float 类型
print((-1) ** 0.5)  # complex类型

# 字符串类型： str 一串普通的文字；用单引号或者双引号包起来

print('你好啊')
print("很高兴认识你")
print('24')  # 这是字符串

# 布尔类型：bool true false
print(4 > 3)  # true
print(2 > 3)  # false

# 列表类型 list
names = ['乔宇婷', '李德码', '撸管男']

print(names)

# 字典类型 dict
person = {'name': '刘亦菲', "age": 18}
print(person)

# 元组类型 tuple
nums = (1, 2, 3, 4)
print(nums)

# 集合类型 set
x = {9, 'hello', True}
print(x)


