#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 16:27

# 遍历：将所有的数据都访问一遍，遍历针对的时可迭代对象

names = ['zansan', 'lisi', 'wangwu', 'zhaoliu', 'ake', 'yingzhneg', 'zhaoliu', 'hangxing', 'huangzhong']

# while / for...in...
for name in names:
    print('我叫{}'.format(name))

# i = 0
# while i < len(names):
#     print('我叫{}'.format(names[i]))
#     i += 1


