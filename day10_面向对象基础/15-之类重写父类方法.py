#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/30 14:29

class Anumal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')



class Person(object):

    def __init__(self, name):
        self.name = name
        self.__money = 1000  # 私有变量

class Dog(Anumal):

    def dance(self):
        print(self.name + "正在跳舞")

    def sleep(self):
        print(str(self.age)+"岁的"+self.name + '正在睡觉')

class Student(Anumal,Person):

    # 重写方法，补充 不要一说到 super 就想到父类！super 指的是 MRO 中的下一个类！
    def __init__(self,name,age,school):
        super(Anumal, self).__init__(name)
        self.school = school

    def study(self):
        print(self.name + "正在学习")


d = Dog('大黄', 2)
s = Student('小王', 12,"北大")

print(Student.mro())

print(s.school)

d.sleep()
d.dance()
s.study()
s.sleep()
