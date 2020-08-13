#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/12 20:23

# python 里的数据类型
# 整形(int) 、浮点型(float)、复数(complex)、字符串(str)、布尔(bool)、列表(list)、元组(tuple)、
# 字典(dict)、集合(set)

# 整形就是整数，计算机只能保存二进制0和1，为了方便数据的表示，同时计算机也支持八进制和十六进制
# 二进制、八进制、十进制、十六进制 在PYTHON里都能表示

a = 98  # 默认数字都是十进制
print(a)

# 以0b开头的数字是二进制
b = 0b1010110101
# print 打印数字的时候。默认是按十进制输出
print(b)

# 0o 开头表示八进制（python3，python2中可以是0开头）
c = 0o23
print(c)

# = 0x 开始表示十六进制
d = 0x34
print(d)
