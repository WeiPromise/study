#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 19:28

# 打印矩形
# for i in range(0, 6):
#     for j in range(0, 8):
#         print('*', end=" ")
#     print()


# 打印三角形
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print('*', end=" ")
#     print()

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d" % (j, i, (i * j)), end="\t")
    print()
