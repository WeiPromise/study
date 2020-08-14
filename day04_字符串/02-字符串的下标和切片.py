#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 10:35

# 下标：索引，表示第几个数据,从0开始
# 可迭代对象：srt list tuple dict set range 都可以遍历
# str list tuple 可以通过下标来获取或操作数据

word = 'zhangsan'  # 字符串：一个一个的字符 串在一起
# 获取指定下标的字符
print(word[4])
# 字符串是不可变的数据类型
# word[4] = 'x'

# 切片：从字符串里复制一段指定的内容，生成一个新的字符串
m = 'hello python i love you'

# 切片语法：m[start:end:setp],开始：结尾：步长（包含头不包含尾）
# 符号只是说明 索引从那边开始计算

print(m[2:9])  # 包含头不包含尾 llo pyt
print(m[2:])  # 没有end,默认到最后 llo python i love you
print(m[:9])  # start,默认从0开始 he
print(m[2::2])  # 每个setp-1次取一个 lopto  oeyu
# print(m[2::0])  # setp不能为0
print(m[2::-2])  # setp为负数，2->9：空字符
print(m[9:2:-2])  # setp为负数，9->2：有数据
print(m[::])  # 从头到尾复制
print(m[::-1])  # 从尾到头复制
print(m[-2:-9])  # 没有数据
print(m[-9:-2])  # 有数据

