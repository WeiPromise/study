#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/6 15:36

# open 参数介绍
# file : 用来指定打开的文件（文件路径）
# mode :打开模式
# encoding : 编码格式


# 路径分为两种：
#   绝对路径：从电脑盘符开始的路径
import os

print(os.name)
print(os.sep)
print(os.path.abspath('xxx.txt'))

# 在python里\标识转义字符

# file = open('C:\develop\python\study\xxx.txt',encoding='utf8')
file = open(r'C:\develop\python\study\day11_文件的操作/xxx.txt', encoding='utf8')
print(file.read())

#   相对路径：当前文件所在的文件夹开始的路径
file = open('xxx.txt', encoding='utf8')
print(file.read())


file.close()
