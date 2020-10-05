#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/29 14:59

class Person(object):

    sex = '男'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 默认方法都是对象方法，用到可self里的属性
    def eat(self,food):
        print(self.name+'正在吃'+food)


    # 如果一个方法没用用到任何self里的任何属性，可以将这个方法写成staticmethod修饰
    @staticmethod
    def sayHello():
        print("hello")

    # 如果这个函数只用到了类属性，我们可以把他定义为类方法
    @classmethod
    def demo(cls):
        print('性别：'+cls.sex)


p = Person('张三',18)

# 实例对象在调用方法是，不需要给形参self传参，会自动把实例对象传递给self

# eat 对象方法，可以直接使用实例对象，方法名(参数)调用
# 使用对象名.方法名(参数)调用的方式，不需要传递参数self
# 会自动将对象名传递参数给self
p.eat('红烧肉')

p2 = Person('李四',29)

p2.eat('锅包肉')

# 对象方法还可以使用类对象调用，类对象.方法名(参数)
# 这种方式，不会自动给self传参，需要手动的指定self
Person.eat(p,"炸洋芋")

print(p.eat)
print(p2.eat)
print(Person.eat)

Person.sayHello()


p.demo()
Person.demo()