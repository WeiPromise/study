#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 19:16

# break：用来结束整个循环
# continue：用例结束本轮循环

# for num in range(1, 6):
#     if num == 4:
#         continue
#     print(num)

# for num in range(1, 6):
#     if num == 4:
#         break
#     print(num)

# 素数

# for...else...语句：当循环里的break没有被执行的时候，就会执行else
for i in range(101, 201):

    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print('%d 是质数' % i)



