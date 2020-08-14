#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 10:52

a = 'abdsjkncjsakcjszbv'

# 长度 len
print(len(a))

# 查找内容相关的方法 find / index / rfind / rindex可以获取指定字符的下标
print(a.find('j'))  # 4 寻找字符第一次出现的索引
print(a.index('j'))  # 4 寻找字符第一次出现的索引
print(a.find('m'))  # -1如果不存在，结果是-1
# print(a.index('m'))  # 如果不存在，报错

print(a.rfind('j'))  # 13 寻找字符最后一次出现的索引,找不到-1
print(a.rindex('j'))  # 13 寻找字符最后一次出现的索引，找不到报错

# startswith/endswith/isalpha/isdigit/isalnum/isspace

print(a.startswith('abs'))  # 以什么字符开头
print(a.endswith('abs'))  # 以什么字符结尾
print(a.isalpha())  # 字符串是字母
print(a.isdigit())  # 是否是数字
print(a.isalnum())  # 至少一个字符
print(a.isspace())  # 是否是空格

# replace方法：用来替换字符串
word = 'hello word'
m = word.replace('l', 'x')  # 替换所有字符
n = word.replace('l', 'z', 1)  # 替换第一个字符
n1 = word[::-1].replace('l', 'p', 1)[::-1]  # 替换最后一个字符
print(word, m, n, n1)

# 修改大小写
# capitalize 第一个单词的首字母大写
print(word.capitalize())
# upper 全部大小
print(word.upper())
# lower 全部小写
print(word.title().lower())
# title 每个单词首字母大写
print(word.title())

# while True:
#     content = input('请输入内容，输入exit退出：')
#
#     print('您输入的内容是：%s' % content)
#     if content.lower() == 'exit':
#         break

# ljust(length)：让字符串一指定长度显示，
# 如果长度不够，默认在右边使用空格补齐,如果长度小于字符串长度，则显示字符串长度
print('hello'.ljust(10))
print('hello'.ljust(10, '#'))
# rjust(length)：让字符串一指定长度显示，
# 如果长度不够，默认在左边使用空格补齐,如果长度小于字符串长度，则显示字符串长度
print('hello'.rjust(10))
# center(length)：让字符串一指定长度显示，
# 如果长度不够，默认在两边使用空格补齐,如果长度小于字符串长度，则显示字符串长度
print('hello'.center(10))

# lstrip():去掉左边的空格
print('  hel   lo  '.lstrip())
# lstrip():去掉右边的空格
print('  hel   lo  '.rstrip())
# lstrip():去掉两边的空格
print('  hel   lo  '.strip())

# 以某种固定格式显示的字符串，我们可以将它们隔成一个列表
x = 'zhangsan+lisi+wangwu+zhaoliu+tianqi'
names = x.split('+')
print(names)
# 将列表转换成字符串
# join():参数是可迭代对象：srt list tuple dict set range
y = '-'.join(names)
print(y)

# 字符串的运算符
# +：拼接
# *：将指定的字符重复N次
# ==：比较两个字符串
# 比较运算：逐个比较字符串的编码值
