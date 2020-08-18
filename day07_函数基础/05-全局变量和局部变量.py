#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/18 15:39

a = 100  # 全局变量，整个python文件都可以使用

word = 'hello'


def my_test():
    x = 'hello'  # 局部变量，只能在函数体内可以用
    print('x = {}'.format(x))

    a = 10  # 如果局部变量名和全局变量同名，会在函数内部又定义一个新的局部变量

    print('函数内部a = {}'.format(a))

    # 通过global 对变量进行申明，可以通过函数修改全局变量函数,也可以申明全局变量
    global  word
    word = 'ok'

    global b
    b = 'hello'

    print('locals = {},globals = {}'.format(locals(),globals()))


my_test()

print('函数外部a = {}，word = {},b = {}'.format(a,word,b))

# 只有函数能分割作用域
# 全局变量，这种最好别用
# if 3 > 2:
#     m = 'hi'
# print(m)