#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/13 21:36
import re

# \s 表示任意的非打印字符

print(re.search(r'\s','hello world \n')) # <_sre.SRE_Match object; span=(5, 6), match=' '>
print(re.search(r'\s','hello\tworld')) # <_sre.SRE_Match object; span=(5, 6), match='\t'>
print(re.search(r'\t','hello\tworld')) # <_sre.SRE_Match object; span=(5, 6), match='\t'>
print(re.search(r'\s','hello\nworld')) # <_sre.SRE_Match object; span=(5, 6), match='\n'>
print(re.search(r'\n','hello\nworld')) # <_sre.SRE_Match object; span=(5, 6), match='\n'>

# \S 表示非空白字符
print(re.search(r'\S',' \t\nw'))  # <_sre.SRE_Match object; span=(3, 4), match='w'>

# ():表示一个分组
n1 = re.search(r'h(\d+)x','sh8234xsafd')
print(n1.group(0)) # h8234x
print(n1.group(1)) # 8234
n2 = re.search(r'h\(.*\)','h(1+1)*2+5')
print(n2) # <_sre.SRE_Match object; span=(0, 6), match='h(1+1)'>

# .：表示匹配除了换行意外的任意字符。如果想要匹配，需要加\

# []: 表示可选项 [x-y]:从x到y区间，包含x和y
print(re.search(r'[0-5f]','pdsf6m')) # <_sre.SRE_Match object; span=(3, 4), match='f'>
print(re.search(r'[0-5f]','pd4sf6m')) # <_sre.SRE_Match object; span=(2, 3), match='4'>
print(re.search(r'[a-f]','pd4sf6m')) # <_sre.SRE_Match object; span=(1, 2), match='d'>

# | :表示或者的关系 和[] 有一定的相似，但有区别
# []:里的值表示区间，单个值
# | 表示可选值，可以是多个值
print(re.search(r'f(x|prz|t)m','pdsfprzm')) # <_sre.SRE_Match object; span=(3, 8), match='fprzm'>

# {} 用来限定出现次数 {m,n},最少出现m次，最多出现n次 {m}:前面的值出现m次
# {m,}出现次数大于等于m
# {,n}出现次数小于等于n
print(re.search(r'[0-5]{3}','pd42m')) # None
print(re.search(r'[0-5]{3}','pd423m')) # <_sre.SRE_Match object; span=(2, 5), match='423'>
print(re.search(r'[0-5]{2,4}','pd422m')) # <_sre.SRE_Match object; span=(2, 5), match='422'>
print(re.search(r'[0-5]{3,4}','pd42m')) # None

# * : 表示前面的元素出现任意次数（0次及以上）等价于{0，}
print(re.search(r'pd[0-5]*m','pd422m')) # <_sre.SRE_Match object; span=(0, 6), match='pd422m'>
print(re.search(r'pd[0-5]*m','pd422234m')) # <_sre.SRE_Match object; span=(0, 9), match='pd422234m'>

# +:表示前面的元素出现至少1次，等价于{1，}
print(re.search(r'go+d','goood')) # <_sre.SRE_Match object; span=(0, 5), match='goood'>
print(re.search(r'go+d','gd')) # None

# ?:两种用法
#   1、规定前面的元素最多只能出现一次，等价于{，1}
print(re.search(r'go?d','goood') ) # None
print(re.search(r'go?d','god')) # <_sre.SRE_Match object; span=(0, 3), match='god'>

# todo  2、将贪婪模式转换为非贪婪模式

# ^：指定内容开头，在[]里表示取反[^0-9]:非数字
# $：指定内容结尾
print(re.search(r'^p.*m$','pd422234m')) # <_sre.SRE_Match object; span=(0, 9), match='pd422234m'>
print(re.search(r'^p.*m$','pd422234mhah')) # None










