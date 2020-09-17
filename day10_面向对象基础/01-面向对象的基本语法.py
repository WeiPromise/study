#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/17 14:54

# 定义类：一般采用大驼峰命名法，每个单词的首字母都大写
# 1.class <类名>
# 2.class <类名>(object)

class Student(object): # 关注这个类有那些属性和行为

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
S1 = Student('非非',27,1.80)
S2 = Student('帮主',27,1.79)

S1.run()
S2.eat()
