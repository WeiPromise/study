#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 10:19

# 可以使用一对单引号、双引号或者一对三个双引号、三个单引号

a = 'hello'
b = "python"
c = """hahaha
不不不
"""  # 可以换行
d = '''呵呵呵
，嘿嘿嘿'''  # 可以换行
print(a, b, c, d)

# 如果字符串里面还有双引号，外面就可以使用单引号
m = 'xiaoming said :"I am xiaoming"'
n = "xiaoming said :I'm xiaoming"
print(m, n)

# 在字符串的前面添加r/R 在python里表示的是原生字符串
x0 = 'hello \teacher'
x = r'hello \teacher'
print(x0, x)
