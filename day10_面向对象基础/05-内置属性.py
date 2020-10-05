#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/28 16:22

class Person(object):
    """
    这是一个人呢
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+'正在吃饭')

p = Person('张三',18)

#dir 把对象的所有属性和行为都列出来
print(dir(p))

# 把对象的属性和值转换成为一个字典
print(p.__dict__) # {'age': 18, 'name': '张三'}
# 获取对象的注释文档
print(p.__doc__) #     这是一个人呢

