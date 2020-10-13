#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/13 23:14

import re

# 字母表示它本身，很多字母面前， \会有特殊含义

# \n :表示换行
# \t ：表示一个制表符
# \s ：空白字符
# \S ：非空白字符
# \d ：表示数字，等价与[0-9]

print(re.search(r'x\d+p','x243p')) # <_sre.SRE_Match object; span=(0, 5), match='x243p'>
print(re.search(r'x[0-9]+p','x243p')) # <_sre.SRE_Match object; span=(0, 5), match='x243p'>

# \D : 表示非数字，等价于[^0-9]
print(re.search(r'\D+','hello0')) # <_sre.SRE_Match object; span=(0, 5), match='hello'>
print(re.search(r'[^0-9]+','hello0')) # <_sre.SRE_Match object; span=(0, 5), match='hello'>

# \w : 表示数字、字母及_以及中文等 非标点符号
print(re.findall(r'\w+','h+E-11.0_X*')) # ['h', 'E', '11', '0_X']


# \W : \w取反
print(re.findall(r'\W+','h+E-11.0_X*')) # ['+', '-', '.', '*']