#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/13 17:35


# 调用 re.match/re.search/re.finditer/re.fullmatch
# 都能拿到re.Match对象

import re

content = 'hello wrold good morining l love you baby good'

m = re.search(r'good',content) # <_sre.SRE_Match object; span=(12, 16), match='good'>

# print(dir(m))
# ['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
# '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', 'end', 'endpos', 'expand', 'group', 'groupdict',
# 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']

# pos
print(m.pos) # 0
# endpos
print(m.endpos) # 46

# span 匹配到的结果字符串的开始和结束下标
print(m.span()) # (12, 16)



#group方法表示正则表达式的分组
# 1、在正则表达式里使用()表示一个分组
# 2、如果没有分组，默认只有一个分组
# 3、分组的下标从0开始

# 获取匹配的字符串结果,可以传参，表示第n个分组，默认第0个
print(m.group()) # good
print(m.group(0)) # good
# print(m.group(1)) # IndexError: no such group

n = re.search(r'9.*0.*5.*7','ak9hf0kj5anaas7fji')
# 四个分组
n1 = re.search(r'(9.*)(0.*)(5.*7)','ak9hf0kj5anaas7fji')
print(n) # 9hf0kj5anaas7
print(n1.group(0)) # 9hf0kj5anaas7 第0组就是把整个正则表达式当做一个整体
print(n1.group(1)) # 9hf
print(n1.group(2)) # 0kj
print(n1.group(3)) # 5anaas7

# 返回元组
print(n1.groups()) # ('9hf', '0kj', '5anaas7')
# 获取到分组组成的字典
n2 = re.search(r'(?P<X1>9.*)(?P<X2>0.*)(?P<X3>5.*7)','ak9hf0kj5anaas7fji')
print(n2.groupdict()) # {'X3': '5anaas7', 'X1': '9hf', 'X2': '0kj'}