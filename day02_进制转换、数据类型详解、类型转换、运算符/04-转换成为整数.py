#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 10:28

# 使用int 内置类可以将数据转换成为整数

a = '31'
b = int(a)

print(a)
print(b)

# print(a+1) 报错
print(b + 1)

# 字符串不是合法的数字，报错
# x = 'hello'
# y = int(x)
# print(y)

# 十六进制需要加标识(数字0-9，字母：a/b/c/d/e/f)
x = '1a2f'
y = int(x, 16)
print(y)

# 八进制(数字0-7组成)
m = '12'
n = int(m, 8)
print(n)
