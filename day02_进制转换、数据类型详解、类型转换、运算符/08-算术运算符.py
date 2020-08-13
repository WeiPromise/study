#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 11:03

# + - * / **(幂) //(整除) %(取余)

# 优先级：** > * / % // > + -
print(1 + 2)  # 3
print(4 - 2)  # 2
print(4 * 2)  # 8
print(4 / 2)  # 2.0
print(9 / 2)  # 4.5(python 2里是4)
print(9.6 // 2)  # 4
print(2 ** 3)  # 8
print(5 % 3)  # 2
print(5.3 % 3)  # 2.3
print(81 ** 1 / 2)  # 40.5
print(81 / 9 ** 2)  # 1
print(81 ** (1 / 2))  # 9.0
