#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/19 21:47

# 1、一个函数作为另一个函数的参数（lambda 表达式）
# 2、一个函数作为另一个函数的返回值

def foo():
    print('我是foo，我被调用了')
    return 'foo'


def bar():
    print('我是bar，我被调用了')
    return foo


x = bar()  # 这里并没有被调用

print('x的值是{}'.format(x))

# 这样就都调用
bar()()


# 3、函数内部再定义一个函数

def outer():
    m = 100

    def inner():
        n = 90
        print('我是inner函数')

    print('我是outer函数')
    return inner

outer()()
