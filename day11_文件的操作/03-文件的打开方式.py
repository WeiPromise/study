#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/6 16:01

# mode：指的是文件的打开方式
# r：只读
# w：写入模式，打开文件以后，只能写入，不能读取，如果文件存在，会覆盖文件，如果不存在，会新建
# b：以二进制的形式打开文件
# t：以文本的形式打开
# rb：以二进制读取，wb：以二进制写入

# a:追加模式，如果文件存在，追加，如果不存在，会创建
# r+：可读写，如果文件不存在，会保存(基本不用)
# w+: 可读写，如果文件存在，会覆盖，如果不存在，会创建(基本不用)

# file = open('../xxx.txt','r',encoding='utf-8')
# print(file.read())
# # file.write('hello')
# file.close()

# file1 = open('../xxx.txt','w',encoding='utf-8')
# file1.write('今天天气好晴朗哦耶')
# # file1.read()
# file1.close()

file = open('xxx.txt', 'rb')
print(file.read())
file.close()

file1 = open('xxx.txt', 'wb')
file1.write('今天天气好晴朗哦耶hahah'.encode('utf-8'))
# file1.read()
file1.close()

