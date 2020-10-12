#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/7 21:08

# 在程序运行过程中，由于编码不规范等造成程序无法正常执行，此时程序就会报错
# 健壮性：很多编程语音都有异常处理机制

# try...except 语句用来处理程序运行过程中的异常

def div(a, b):
    try:
        return  a / b
    except Exception as e:
        print('出错了!!!! {}'.format(e))
        exit(1)

x = div(5, 0)

x += 3

print(x)
