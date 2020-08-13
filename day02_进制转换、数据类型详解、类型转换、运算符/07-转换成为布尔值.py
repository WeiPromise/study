#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 10:47

# bool 内置类可以将数据转换成为布尔

print(bool(100))  # True
print(bool(-1))  # True
# 只有0 其他数字都是True
print(bool(0))  # False

print(bool('gello'))  # True
print(bool('False'))  # True
# 只有空字符串为False,其他都是True
print(bool(''))  # False

# None 也是False
print(bool(None))  # False

# 空列表/空元组/空字典/空集合也是False
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(set()))  # False

# 再计算机里，True  和False 分别是1和0
print(True + 1)
print(False + 1)

# 隐式类型转换
if 3:
    print("hello")

if 0:
    print("hahah")
