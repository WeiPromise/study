#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/9 14:12


try:
    with open('xxx.txt','r',encoding='utf-8') as file:
        print(file.read()) # 需要要再手动关闭文件
        #file.close() # with 关键字帮助我们关闭文件
except FileNotFoundError as e:
    print(e)


# whit我们称之为上下文管理器，很多需要手动关闭的链接
# 比如说，文件链接，socket链接，数据库的链接都能使用with 关键字自动关闭链接
# whit关键字后面对象，需要实现__enter__和__exit__魔法方法
# 当进入到with代码块时，会自动调用__enter__方法
# 当with代码块执行完成之后，会自动调用__exit__方法


class Demo(object):

    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('__enter__方法被调用了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被调用了')

    def __repr__(self):
        print('name:{}'.format(self.name))

def create_obj():
    return Demo('zhangsan')


with create_obj() as d:
    print(d)

