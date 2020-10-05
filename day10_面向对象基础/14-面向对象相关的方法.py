#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/30 14:17

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person1(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def study(self):
        print(self.name + "正在学习")



p1 = Person('张三', 18)
p2 = Person('李四', 15)

# 获取两个对象的内存地址 id(p1) == id(p2)
print(p1 is p2) # is 身份运算符，用来比较是否是同一个对象


s = Student('王五',12)
# isinstance 判断一个实例是否是指定的类对象或者其父类实例化出来的
if isinstance(s,Person):
    s.study()
if isinstance(s,(Person,Person1)):
    s.study()


# 判断一个类是否是另是另一个类的子类
print(issubclass(Student,Person))
