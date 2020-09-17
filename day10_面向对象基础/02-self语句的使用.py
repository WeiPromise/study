#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/17 15:13

class Student(object): # 关注这个类有那些属性和行为

    # 这个属性直接定义在类里，是一个元组，用来规定对象可以存在那些属性
    __slots__ = ('name','age','height')

    # 在__init__(self)方法里，以参数的形式定义特征，我们称之为属性
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    # 行为定义为一个个函数
    def run(self):
        print('{}正在跑步'.format(self.name))

    def eat(self):
        print('正在吃饭')


# Student() ==> 会自动调用__init__方法
# 1.调用__new__方法，申请内存空间
# 2.调用__init__方法，并让self指向申请好的那段内存空间
# 3.让S1也指向创建好的内存空间
# 4.类里所有方法会统一存放在一块内存，供self去调用
S1 = Student('非非',27,1.80)
print(S1.name)

S2 = Student('帮主',27,1.79)

S1.run()
S2.eat()

# 动态属性 配合 __slots__方法使用
# 直接使用等号给一个属性赋值
# 如果这个属性不存在，会添加属性
# 如果存在，会重新赋值
S1.age = 30
# S1.sex = '男'
print(S1.age)
# print(S1.sex)

