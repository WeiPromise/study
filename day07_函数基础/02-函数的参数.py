#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/18 14:53

# def 函数名(参数)：
#   函数体
#  调用函数：函数名(参数)

def tell_story(addr):
    print('从前有座山')
    print('山上有个{}'.format(addr))
    print('庙里有两个和尚在讲故事')
    print('大和尚让小和尚讲')
    print('小和尚让大和尚讲')


age = int(input('请输入年龄: '))

if 0 <= age < 3:
    for i in range(5):
        tell_story('庙')
elif 5 > age >= 3:
    tell_story('河')
