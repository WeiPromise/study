#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/8 15:53

# file = open('xxx.txt','rb')
#
# try:
#     while True:
#         content = file.read(1024)
#
#         if not content:
#             break
#         print(content)
# # 无论如何，finally下的代码一定会执行
# finally:
#     print('关闭流')
#     file.close()


def demo(a, b):
    try:
        x = a / b
        return x
    except Exception as e:
        print(e)
        exit(1)
    finally: # 如果函数里有finally,finally里的返回值会覆盖之前的返回值
        return 0


print(demo(4, 2))  # 0
print(demo(1, 0))  # 0
