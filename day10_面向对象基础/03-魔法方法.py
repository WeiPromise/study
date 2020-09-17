#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/17 16:26

# 魔法方法，也叫魔术方法，是类里的特殊的一些方法
# 特点：
# 1、不需要手动调用，会在合适的时机自动调用
# 2、这些方法，都是使用__开始，使用__结束
# 3、方法名都是系统规定好的，在核实的时机自己调用


class Person(object):

    def __init__(self, name, age, height):
        # 在创建的对象时，会自动调用
        print('在创建的对象时，__init__自动调用')
        self.name = name
        self.age = age
        self.height = height

    def __del__(self):
        # 在对象被销毁时(程序结束)，会自动调用
        print('在对象被销毁时，__del__自动调用')

    # 直接对象()时，就会调用这个方法
    def __call__(self, *args, **kwargs):
        fn = kwargs.get('fn')
        return fn(args[0],args[1])


    def __str__(self):
        return "name={},age={},height={}".format(self.name,self.age,self.height)




p = Person('非非',27,1.80)

# 可以手动销毁
# del p

print("====================")
# 当打印一个对象的时候，会调用这个对象的__str__ 或者 __repr__方法
# __repr__ 更注重正确性，_str__ 更注重可读性(用得较多)
# 如果两个方法都写了，会选择__str__
print(p)

# __call__方法可以直接 对象名()==>调用这个对象的__call__方法
print(p(6,2,fn = lambda x,y:x*y))