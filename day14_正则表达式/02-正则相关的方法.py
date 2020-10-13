#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/13 16:55


import re
from collections import Iterable

# 查找字符串，返回的结果是一个re.Match对象
#   match
#   search
#   共同点：1、只对字符串查询一次，2、返回值类型都是re.Match对象
#   不同点：match是从头开始匹配，一旦匹配失败，就返回None；search是在整个字符串里匹配，匹配到为止，匹配不到返回None
# finditer : 查找到所有的匹配数据，放到一个可迭代对象里，可迭代对象的值是re.Match对象
# findall : 查找到所有的匹配数据，放到一个列表里，列表里的值就是匹配值
# fullmatch ：是从头到结尾，完全匹配返回re.Match对象，否则返回None

content = 'hello wrold good morining l love you baby good'

m1 = re.match(r'hello',content) # <_sre.SRE_Match object; span=(0, 5), match='hello'>
m2 = re.search(r'hello',content) # <_sre.SRE_Match object; span=(0, 5), match='hello'>

print(m1,m2)

m3 = re.match(r'good',content) # None
m4 = re.search(r'good',content) # <_sre.SRE_Match object; span=(12, 16), match='good'>
m5 = re.search(r'goodhah',content) # None
print(m3,m4,m5)


# finditer 返回的结果是一个可迭代对象

n1 = re.finditer(r'good',content)
print(isinstance(n1,Iterable)) # True

print(n1) # <callable_iterator object at 0x000001833E416D30>

# t:
#   <_sre.SRE_Match object; span=(12, 16), match='good'>
#   <_sre.SRE_Match object; span=(42, 46), match='good'>
for t in n1:
    print(t)


# findall
n2 = re.findall(r'good',content)
print(n2) # ['good', 'good']

# fullmatch
n3 = re.fullmatch(r'good',content)
print(n3) # None

n4 = re.fullmatch(r'hello wrold good morining l love you baby good',content)
print(n4) # <_sre.SRE_Match object; span=(0, 46), match='hello wrold good morining l love you baby good'>

n5 = re.fullmatch(r'hello.*good',content)
print(n5) # <_sre.SRE_Match object; span=(0, 46), match='hello wrold good morining l love you baby good'>




