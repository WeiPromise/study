#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/30 11:27

# 手动指定继承至object
class Student(object):
    pass

# python3 默认继承至object
class Dog:
    pass


# 新式类：继承至object的类
# 经典类：不继承至object的类

# 区别，python2里，如果不指定继承至object,这个类就是一个经典类
# python3里，不存在经典类，都是新式类