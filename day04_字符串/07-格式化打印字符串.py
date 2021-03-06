#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 15:23

# 可以使用 % 占位符表示格式化一个字符串

name = '张三'
age = 18

# %s ==> 字符串
# %d ==> 整数
# %nd ==> 显示n位，如果不够，前面使用空格补齐
# %-nd ==> 显示n位，如果不够，后面使用空格补齐
# %0nd ==> 显示n位，如果不够，前面使用0补齐
# %f ==> 浮点
# %.nf ==> 浮点，保留n位小数
# %x ==> 将数字以十六进制输出（基本不用）
print('大家好，我叫%s，我今年%d岁' % (name, age))
print('大家好，我叫%s，我今年%3d岁' % (name, age))
print('大家好，我叫%s，我今年%-3d岁' % (name, age))
print('大家好，我叫%s，我今年%03d岁' % (name, age))
print('大家好，我叫%s，我今年%03d岁' % (name, age))
print('大家好，我叫%%s，我今年%03d岁' % age)
print('大家好，我叫%s，我今年%.2f岁' % (name, 3.1415934))
print('%x' % 255)

# ======================================================
# {} 也可以进行占位
x = '大家好，我是{}，我今年{}岁'.format('张三', 19)
print(x)
# {数字} 根据数字的顺序来进行填入，数字从0开始
y = '大家好，我是{1}，我今年{0}岁'.format(23, '张三')
# {变量名}
z = '大家好，我是{name}，我今年{age}岁'.format(age=23, name='张三')

# 混合使用 {数字} {变量}
m = '大家好，我是{1}，我今年{0}岁，我来自{local}'.format(23, '张三', local="中国")

# format 参数，变量放最后
# n = '大家好，我是{1}，我今年{0}岁，我来自{local}'.format(local="中国", 23, '张三')

# {} 什么都不写和{数字}不能混合使用

# {} 什么都不写和{变量} 混合使用 ,不推荐使用
# n = '大家好，我是{name}，我今年{}岁，我来自{}'.format(23, '中国', name="李四")

d = ['张三', 18, '上海']
info = {'name': '李四', 'age': 18, 'addr': '武汉'}
# *d 拆包list
# **d 拆包dict
b = '大家好，我是{}，我今年{}岁，我来自{}'.format(*d)
# 顺序不能乱
# b = '大家好，我是{2}，我今年{1}岁，我来自{0}'.format(*d)
c = '大家好，我是{name}，我今年{age}岁，我来自{addr}'.format(**info)

print(x, y, z, m, b, c, sep='\n')
