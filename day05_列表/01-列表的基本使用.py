#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 15:55

# 当我们有很多数据需要保存的时候，我们可以考虑列表

# 使用中括号[]表示一个列表，里面一个数据表示一个元素，元素之间使用逗号分隔
names = ['zansan', 'lisi', 'wangwu', 'zhaoliu']

# list(可迭代对象)：srt list tuple dict set range 转换为一个列表
name01 = list(('zansan', 'lisi', 'wangwu', 'zhaoliu'))

print(name01)

# 可以使用下标获取元素、对元素进行切片，修改元素
names[3] = 'tianqi'

# 切片

sub = names[1:3]

print(names, sub, sep='\n')
