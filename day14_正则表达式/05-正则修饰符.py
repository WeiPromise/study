#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/13 18:41

import re

content = 'sdfmo\neasd'
# 正则修饰符是对正则表达式进行修饰
# .:表示除了换行以外的任意字符
m = re.search(r'm.*a',content)
print(m) # None


# re.S : 让.匹配换行
n = re.search(r'm.*a',content,re.S)
print(n) # <_sre.SRE_Match object; span=(3, 8), match='mo\nea'>

# re.I:忽略大小写
y = re.search(r'x','good Xyz',re.I)
print(y) # <_sre.SRE_Match object; span=(5, 6), match='X'>

# \w:表示的是字母数字和_，+：出现一次以上，$：以指定的内容结尾
z = re.search(r'\w+$','l am boy \n you are girl \n he is a dog')
print(z) # <_sre.SRE_Match object; span=(34, 37), match='dog'>

# re.M : 让^/$能够匹配到换行
z1 = re.findall(r'\w+$','l am boy\n you are girl\nhe is a dog',re.M)
print(z1) # ['boy', 'girl', 'dog']