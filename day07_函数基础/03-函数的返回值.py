#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/18 15:10

# 返回值就是函数执行的结果，并不是所有函数都需要返回值

# 求和 -> 指定返回值类型
def my_sum(a:int, b:int) -> int:
    """
    函数求和
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    return a + b


print(my_sum(2, 5))
