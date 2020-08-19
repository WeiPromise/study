#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/19 11:16

# 递归：简单来说，就是函数内部自己调用自己

count = 0


def tell_story():
    global count
    count += 1
    print('从前有座山')
    print('山上有个庙')
    print('庙里有两个和尚在讲故事')
    print('大和尚让小和尚讲')
    print('小和尚让大和尚讲')
    if count <= 5:
        tell_story()


# tell_story()

# 求1->的和

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)


print(sum_n(10))


# 阶层
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# 斐波拉契
def fibonacci(n):
    if n in [1,2]:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(12))