#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/7 20:22

# python 里存入数据只支持存入字符串和二进制
# json: 将python里的数据(str/list/tuple/dict/int/float/bool/None)等转换成对应的字符串
# pickle: 将python里任意的对象转换成为二进制

import pickle

# 序列化：
#   dumps:将数据转换成为二进制,不会将数据保存到文件里
#   dump：将数据转换成为二进制的同时写入文件
# 反序列化：
#   loads ：将二进制加载成为Python里的数据
#   load：读取文件，把读取的二进制内容加载成为Python里的数据

names = ['zhangsan','lisi','wangwu','zhaoliu']
# b_names = pickle.dumps(names)
#
# file = open('names.txt','wb')
# # 这样写打开视觉效果是有问题的，不要管就对了
# file.write(b_names)
#
#
# file.close()

# file1 = open('names.txt','rb')
# x = file1.read()
# y = pickle.loads(x)
# print(y)
# file1.close()

# file2 = open('names.txt','wb')
# pickle.dump(names,file2)
# file2.close()
#
# file3 = open('names.txt','rb')
# print(pickle.load(file3))


class Dog(object):
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def eat(self):
        print('{}正在吃东西'.format(self.name))

d = Dog('大黄','黄')
# 保存到文件里面
pickle.dump(d,open('dog.txt','wb'))

# 从文件里加载出来
dd = pickle.load(open('dog.txt','rb'))

print(dd.name,dd.color)
dd.eat()


# pickle 和json区别？什么情况下使用json，什么情况下用pickle？
# pickle：用来将数据原封不动的转换成为二进制。但是这个二进制，只能在python里识别
# json：只能保存一部分信息，作用是用来在不用平台里传递数据。json里储存的数据都是基本的数据类型
