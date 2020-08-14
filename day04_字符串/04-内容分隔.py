#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 11:31

# split splitlines partition rpartition

# 字符串类型的数据

x = 'zhangsan-lisi-wangwu-zhaoliu-tianqi'

# split 切割以后是一个list
y = x.split('-')
y1 = x.split('-', 2)
z = x.rsplit('-')
z1 = x.rsplit('-', 2)
print(x, y, y1, z, z1, sep="\n")

# partition 指定一个字符串作为分隔附，分为三部分
# 前面 分隔符 后面
print('aadnmsabcidas'.partition('abc'))  # ('aadnms', 'abc', 'idas')
print('aadnmnsabcmnidas'.partition('mn'))  # ('aadn', 'mn', 'sabcmnidas') 第一次出现分隔
print('aadnmnsabcmnidas'.rpartition('mn'))  # ('aadnmnsabc', 'mn', 'idas') 最后一次出现分隔

print('asncjh\nancajk\nnc'.splitlines(
    False))  # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符,默认为 False。
