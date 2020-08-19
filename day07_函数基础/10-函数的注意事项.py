#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/19 11:07

# 函数的三要素：函数名、参数、返回值
# 在python中：不允许函数的重名；如果函数重名，后一个函数会覆盖前一个函数
# python里，函数名也可以理解成为一个变量名，不能定义变量和函数名一致，如果有，后面的变量会覆盖掉函数
# 要避开内置函数名

def my_test(a,b):
    print(a+b)

# def my_test(a):
#     print(a)

# my_test = 5

my_test(12,23)