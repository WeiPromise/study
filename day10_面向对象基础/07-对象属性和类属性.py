#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/29 11:14

# Person 类对象
class Person(object):

    # 类属性
    type = '人类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 对象p,p1是通过Person类创建出来的实例对象
# 实例对象的属性叫对象属性
p = Person('张三',18)
p1 = Person('李四',18)

print('0x%X' % id(p)) # 0x21186D0C5F8
print('0x%X' % id(p1)) # 0x21186D0C978


# 类对象
print('0x%X' % id(Person)) # 0x1A9B12B7A88
# 类属性
print(Person.type)


# 实例对象本身不保存类属性，它会通过去找类对象去拿到
print(p1.type)
print(p.type)

# 类属性只能通过类对象来修改
Person.type = '重点人'

# 通过实例对象只是给自己增加了一个对象属性
p1.type = "p1人"

print(Person.type)
print(p.type)
print(p1.type)











