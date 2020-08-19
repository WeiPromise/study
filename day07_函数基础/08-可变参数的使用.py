#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/19 10:35

# 可变参数：
#   *+变量名：表示可变参数；可变参数必须放在位置参数后面
#   可变参数后面只能跟缺省参数，且调用时缺省参数必须使用关键字参数指定
#   **kwargs:表示可缺省的关键字参数，字典形式存在
def add(init,*args,name='tom',**kwargs):
    print(name,type(args))
    print(kwargs)
    sum = init
    for i in args:
        sum += i
    return sum


print(add(20,1, 2, 5, 7, 5,name='jack'))
print(add(20,1, 2, 5, 7, 5))
print(add(20,1, 2, 5, 7, 5,name='tom',x=1,y=2))
