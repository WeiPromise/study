#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/29 14:24

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 私有变量

    def set_money(self, num):
        # 验证逻辑
        self.__money = num

    def get_money(self):
        # 操作提醒
        return self.__money


p = Person('张三', 18)

print(hex(id(p)))  # 0x1e3601864e0

print(p.name)
print(p.age)

# 两个下划线开始的变量是私有变量，两个下划线开始的函数是私有函数，不能直接获取
# print(p.__money)
# 获取方法：
# 1、使用对象._类名__私有变量名获取
print(p._Person__money)
# 2、定义get和set方法获取
p.set_money(10000)

print(p.get_money())

# 3、使用property来获取
