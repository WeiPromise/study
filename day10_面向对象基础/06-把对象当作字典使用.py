#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/29 11:02


class Person(object):
    """
    这是一个人呢
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 对象当字典用
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

p = Person('张三',18)

# 将对象转换为字典
print(p.__dict__)

# []语法会调用对象的__setitem__方法
p['age'] = 20

print(p.__dict__)

# 会调用__getitem__方法
print(p['age'])