#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 11:38

# 与and(&) 或or 非not

print(3 > 2 and 3 > 1)
print(3 > 2 and 3 > 5)
print(3 > 2 or 3 > 5)
print(not (3 > 5))
print(3 > 2 & 3 > 1)
# print(3 > 2 | 3 > 1)

# 短路
4 > 3 and print("hello")
4 > 5 and print("python")

4 > 3 or print("hello1")
4 > 5 or print("python1")

# 逻辑运算的结果不一定是bool
#  与运算，取第一个为false的值，所有都为true,取最后一个的值
print(3 and 5 and 0 and 'hello')  # 0
print(3 and 5 and 2 and 'hello')  # hello
#  或运算，取第一个为true的值，所有都为false,取最后一个的值
print(0 or [] or 5 or 'hahah')  # 5
print("" or [] or {} or 0)  # 0

