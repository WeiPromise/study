#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/18 16:05

def my_test(a, b):
    x = a // b
    y = a % b

    # 一般情况下，一个函数最多只会执行一个return语句
    # 特殊情况（finally）下，一个函数可能会执行多个return语句

    # return {'x':x,'y':y}
    # return [x,y]
    # return (x, y)
    return x, y  # 返回本质是一个元组，元组用得多


result = my_test(13, 5)

print('商是：{},余数是：{}'.format(result[0], result[1]))

shang, yushu = my_test(17, 3)
print('商是：{},余数是：{}'.format(shang, yushu))

