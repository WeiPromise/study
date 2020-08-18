#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/18 14:44

# 函数就是一堆准备好的代码，在需要的时候调用这一堆代码


# def 函数名(参数)：
#   函数体

def tell_story():
    print('从前有座山')
    print('山上有个庙')
    print('庙里有两个和尚在讲故事')
    print('大和尚让小和尚讲')
    print('小和尚让大和尚讲')


age = int(input('请输入年龄: '))

if 0 <= age < 3:
    for i in range(5):
        tell_story()
elif 5 > age >= 3:
    tell_story()
