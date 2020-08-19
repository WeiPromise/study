#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/19 18:18

# 有几个内置函数和内置类，用到了匿名函数
# ================ 排序 =========================
nums = [4, 8, 5, 87, 33, 32]
# nums.sort()
# print(nums)

# sorted内置函数，不会改变原有的数据，而是生成一个新的有序的列表
x = sorted(nums)
print(x)

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 652.5},
    {'name': 'lisi', 'age': 23, 'score': 658.5},
    {'name': 'wanngwu', 'age': 20, 'score': 632.5},
    {'name': 'zhaoliu', 'age': 19, 'score': 552.5},
    {'name': 'tianqi', 'age': 27, 'score': 659.5},
    {'name': 'laoba', 'age': 18, 'score': 672.5}
]

#  students.sort()
#  TypeError: unorderable types: dict() < dict()
# print(students)
students.sort(key=lambda student: student['score'])
print(students)

# ============================filter 内置类的使用==============================

# filter对可迭代对象进行过滤，得到的是一个filter对象
# python2是一个内置函数，3中是一个内置类

ages = [12, 15, 18, 34, 24, 45, 76]
# 参数第一个是过滤条件，第二个是可迭代对象
x = filter(lambda ele: ele >= 18, ages)
ad = list(x)
print(ad)

# ============================map 内置类的使用=================
m = map(lambda ele:ele+2,ages)
print(list(m))

# ====================reduce =================
# reduce 以前是一个内置函数，现在在functools 模块里面
# 内置函数和内置类都在builtins.py里面

from functools import reduce

sum_ages = reduce(lambda ele1,ele2:ele1+ele2,ages)
# 参数是对象时，第一个元素是返回值，第二个参数是对象，需要指定初始值，这里是0
sum_ages1 = reduce(lambda ele1,ele2:ele1+ele2['age'],students,0)

print(sum_ages)
print(sum_ages1)


# ====================all=============
# 如果所元素转化成bool值全为true则返回true

# ====================any=============
# 如果有一个元素转化成bool值为true则返回true

