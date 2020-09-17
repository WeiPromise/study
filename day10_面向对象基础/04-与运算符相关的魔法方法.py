#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/17 16:56


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def  __eq__(self, other):
        return self.name == other.name and self.age == other.age

p1 = Person('znagsan',18)
p2 = Person('znagsan',18)

# p1和p2是同一个对象吗？不是

print('0x%X' % id(p1)) # 0x26E6A85C978
print('0x%X' % id(p2)) # 0x26E6A85CE10

# 身份运算符 is 判断两个对象是否是同一对象

print(p1 is p2)
print(p1 == p2)


num1 = [1,2,3]
num2 = [1,2,3]
# is 比较地址
# == 回调用对象的__eq__方法，获取这个方法的比较值(不重新__eq__时，默认比较地址)
print(num1 is num2)
print(num1 == num2)