#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/29 15:48


class Singleton(object):

    __instance = None

    __is_first = True

    @classmethod
    def __new__(cls, *args, **kwargs):
        # 申请内存，创建一个对象，并把对象的类型设置为cls
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,a,b):
        if self.__is_first:
            self.a = a
            self.b = b
            self.__class__.__is_first = False

# 调用__new__ 方法申请内存,重写__new__
s1 = Singleton('hehe','111')
s2 = Singleton('haha','222')

# 对象后创建的实例会覆盖前面创建的对象，这样不行
print(s1.__dict__)
print(s2.__dict__)

print(s1 is s2)