#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/30 15:23

# 多态是基于继承，通过子类重写父类的方法
# 达到不同的子类对象调用相同的父类方法，得到不同的结果
# 提高代码的灵活性



class PoliceDog(object):
    def attack_enemy(self):
        print('警犬正在攻击坏人')


class BlindDog(object):
    def lead_road(self):
        print('导盲犬正在领路')


class Person(object):
    def __init__(self,name):
        self.name = name

    def work_with_pd(self):
        print(self.name+'正在工作')
        self.dog.attack_enemy()

    def work_with_bd(self):
        print(self.name+'正在走路')
        self.dog.lead_road()

pd = PoliceDog()

pd1 = BlindDog()
poloce = Person('张警官')

poloce.dog = pd1
poloce.work_with_bd()



