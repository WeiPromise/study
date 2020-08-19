#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/19 10:17

# 缺省参数：
# 有些函数的参数是，如果你传递了参数，就使用传递的参数,如果没有传递参数，就使用默认参数
# 缺省参数的定义：在函数申明的时候，给参数一个初始值就行，如下面函数中的属性city;
# 缺省参数必须放在位置参数的最后面
def say_hello(name,age,city='北京'):
    print('大家好，我是{},我今年{}岁，我来自{}'.format(name,age,city))

say_hello('jack',18,'大连')

# 如果有位置参数和关键字参数，关键字参数一定要放在位置参数的后面
say_hello('tom',age=19)
# say_hello(name='tom',19)
# say_hello(age=19,'tom')