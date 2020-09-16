#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/16 14:32

# random : 生成一个随机数

import random

# 生成一个 A到B的随机整数 [a,b]
print(random.randint(2,9))

# 生意 [0,1)的随机浮点数
print(random.random())

# 用来生成[a,b)的随机整数，最后一个参数是每个几个生成一个
print(random.randrange(0,9,3))

# 用来在可迭代对象里随机抽取一个数据
print(random.choice(['zhangsan','lisi','wangwu']))

# 用来在可迭代对象里随机抽取n个数据组成一个新的可迭代对象
print(random.sample(['zhangsan','lisi','wangwu','zhaoliu','tianqi'],2))

