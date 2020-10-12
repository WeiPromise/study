#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/7 17:59

# 序列化：将数据从内存持久化保存到硬盘的过程
# 反序列化：将数据硬盘加载到内存的过程

# 只能写入字符串或者二进制文件
# 字典，列表，数字等都不能直接写入到文件中
# 将数据转换成字符串：repr/str 使用json模块
# json本质就是字符串，区别在于json里要用双引号表示字符串
# 将数据转换成为二进制,使用pickle模块

import json

# 序列化
# file = open('neme.txt','w',encoding='utf-8')

# names = ['zhangsan','lisi','wanggwu','zhaoliu']
# dumps:将数据转换成为字符串,不会将数据保存到文件里
# x = json.dumps(names)
# print(x)

# dump:将数据转换成为字符串的同时写入文件
# json.dump(names,file)

# file.close()

# 反序列化

# loads:将json字符串加载成为Python里的数据
# load:读取文件，把读取的内容加载成为Python里的数据

x = '{"name":"zhangsan","age":"17"}'
p = json.loads(x)
print(p['name'])

file1 = open('neme.txt','r',encoding='utf-8')
y = json.load(file1)
print(y)
print(y[0])
file1.close()
