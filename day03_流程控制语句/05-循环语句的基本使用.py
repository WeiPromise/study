#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 18:35

# 循环分为while 循环和for循环
# 不支持 do...while循环

# range :左闭右开 [ )
# for ... in ... in必须是可迭代对象：字符串、列表、字典、元组、集合、range

for n in range(0, 10):
    print('hello python')


num = 0
while num < 10:
    print('hello while')
    num += 1
