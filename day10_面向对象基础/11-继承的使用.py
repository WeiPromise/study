#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/29 16:44

# 面向对象编程的三大特点：封装、继承、多态
# 封装：函数是对语句的封装
# 继承：类和类之间可以人为手动的简历父子关系，父类的属性和方法，之类可以使用
# 多态：是一种技巧，提高代码的灵活性

# 继承的特点：
# 1、

class Anumal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')

class AnumalTow(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '是精神小伙，不需要睡觉')


class Dog(Anumal):
    def dance(self):
        print(self.name + "正在跳舞")

    def sleep(self):
        print(str(self.age)+"岁的"+self.name + '正在睡觉')


# python 支持多继承，两个父类有共同方法，就近原则(数结构：一个父节点的父节点及他的所有父节点都找完在找第二个父)
class Student(AnumalTow,Anumal):

    def study(self):
        print(self.name + "正在学习")


d = Dog('大黄', 2)
s = Student('小王', 12)


d.sleep()
d.dance()
s.study()
s.sleep()


