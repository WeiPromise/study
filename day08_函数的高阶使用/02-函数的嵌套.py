#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/15 15:28

def outer(x: int):
    m = 100  # 局部变量
    print('我是outer函数')

    def inner():  # inner是定义在outer函数内部的一个函数
        print('我是inner函数')

    if x > 18:
        inner()

    return 'hello'


# print(m)
# inner()
outer(12)
print('======================')
outer(21)


# 闭包 = 函数块+ 引用环境
def outer1():
    x = 10  # 在外部函数里定义一个局部变量x

    def inner():
        nonlocal x # 此时，这里x不在是新增的变量，而是外部的局部变量x
        y = x + 1
        # global x = 20
        x = 20
        print(y)
    return inner

outer1()()