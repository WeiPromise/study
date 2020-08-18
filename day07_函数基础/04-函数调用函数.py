#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/18 15:25


# 求和 -> 指定返回值类型
def my_sum(a: int, b: int) -> int:
    """
    函数求和
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    return a + b


def sum_factorial(a: int) -> int:
    sum = 0
    for i in range(a + 1):
        sum = my_sum(sum, i)
    return sum


print(sum_factorial(100))