#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 11:20

# = 号在计算机里是复制运算符，右边的复制给左边
a = 4

b = 'haha'

print(a)
print(b)

x = 1
print(x)
x = x * 2
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x **= 3
print(x)
x //= 3
print(x)

# 特殊场景
a = b = c = d = 10
print(a, b, c, d, sep=",")

# 拆包，等号两边数量要一致
# m, n = 3, 5, 5
m, n = 3, 5

print(m, n)

x = 'hello', 'nihao'
print(x)

# *表示可变长度
# o, *p, q = 1, 2, 3, 4, 5
o, p, q = 1, 2, (3, 4, 5)
print(o, p, q)  # 1 [2, 3, 4] 5


