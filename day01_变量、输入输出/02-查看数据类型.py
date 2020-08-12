#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/12 18:12

a = 34
b = 'hello'
c = True
d = ['tom', 'jack']

# 使用type内置类可以查看一个变量的数据类型

print(type(a))  # <class 'int'> 整数
print(type(b))  # <class 'str'> 字符串
print(type(c))  # <class 'bool'> 布尔
print(type(d))  # <class 'list'> 列表
print(type(3.14))  # <class 'float'> 浮点

# python 里，变量是没有数据类型的，我们所说的变量的数据类型，其实是 变量对应的值的数据类型
x = 23
print(type(x))  # <class 'int'>
x = 'hello'
print(type(x))  # <class 'str'>
