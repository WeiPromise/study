#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 15:20

# in 和 not in 运算符
# 用来判断一个内容在可迭代对象里是否存在

word = 'hello'

x = input('请输入一个字符：')

if x in word:
    print('存在')
else:
    print('不存在')
