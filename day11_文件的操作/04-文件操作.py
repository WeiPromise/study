#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/6 17:48

# file = open('../xxx.txt','rb',encoding='utf-8')
file = open('xxx.txt', 'rb')
# print(file.read())
# file.write('hello')

# 将内容一行行读出来
while True:
    # content = file.readline()
    content = file.read(1024)
    print(content)
    if content == '':
        break


# 将内容读到一个列表中
# contents = file.readlines()
# for content in contents:
#     if len(content.strip())>0:
#         print(content)


# 指定读取的长度
# x = file.read(4)
# print(x)
# file.close()