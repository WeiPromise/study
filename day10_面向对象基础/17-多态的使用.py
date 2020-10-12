#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/6 15:04


class Dog(object):

    def work(self):
        pass

class PoliceDog(Dog):

    def work(self):
        print('警犬正在攻击坏人')


class BlindDog(Dog):

    def work(self):
        print('导盲犬正在领路')


class Person(object):
    def __init__(self,name):
        self.name = name
        self.dog = None

    def work_with_dog(self):
        print(self.name+'正在工作')
        if self.dog is not None and isinstance(self.dog,Dog):
            self.dog.work()


p = Person('张三')


p1 = PoliceDog()

p.dog = p1

p.work_with_dog()


p2 = BlindDog()
p.dog = p2
p.work_with_dog()

