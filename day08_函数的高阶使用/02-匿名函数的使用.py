#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/19 17:46

def add(a: int, b: int) -> int:
    return a + b


print(add(4, 5))  # 函数名(实参) 作用是调用函数，获取到函数的执行结果，并打印

fn = add  # 相当于给函数add 起一个笔名

print(fn(2, 3))

#  除了使用def 关键字定义一个函数以外，还可以使用lambda表达式定义一个函数

#  匿名函数
#  用来表达一个简单的函数，函数调用的次数很少，基本上就是调用一次
#  调用的方式：
#       1、给它定义一个名字（基本不这么用）
#       2、把这个函数当作参数传给另一个函数使用（使用场景比较多）

mul = lambda a, b: a + b  # 匿名函数，基本上只调用一次
print(mul(3, 9))


def calc(a, b, fnu):
    return fnu(a, b)


print(calc(2, 3, lambda a, b: a + b))
print(calc(2, 3, lambda a, b: a * b))
