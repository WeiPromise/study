#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/9 14:51

# 系统内置的异常：ZeroDivisionError,FileNotFoundError......
#


class MyException(Exception):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '密码长度应该在{}到{}位'.format(self.x,self.y)


password = input('请输入您的密码：')

if 6 <=len(password) <=12:
    print('密码正确')
else:
    # 使用raise关键字可以抛出一个异常
    raise MyException(6,12)
# 保存
print('保存数据')
