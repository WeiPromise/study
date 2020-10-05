#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/29 17:13

# 面向对象编程的三大特点：封装、继承、多态
# 封装：函数是对语句的封装
# 继承：类和类之间可以人为手动的简历父子关系，父类的属性和方法，之类可以使用
# 多态：是一种技巧，提高代码的灵活性

class Anumal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__sex = '男'

    def sleep(self):
        print(self.name + '正在睡觉')

    def __demo(self):
        print('这是父类Anumal的私有方法')


class Dog(Anumal):
    def dance(self):
        print(self.name + "正在跳舞")

    def sleep(self):
        print(str(self.age)+"岁的"+self.name + '正在睡觉')

    def __test(self):
        print('这是之类Dog的私有方法')

d = Dog('大黄',3)

print(d.name)

d._Dog__test() #自己类里定义的私有方法，对象名._类名__私有方法名()；
# 私有属性和方法之类没有继承
# d._Dog__demo() # 父类的私有方法，之类没有继承
# print(d._Dog__sex())