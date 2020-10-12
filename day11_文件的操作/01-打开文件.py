#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/6 15:26

# python 使用 open 内置函数打开并操作文件

# open 参数介绍
# file : 用来指定打开的文件（文件路径）
# mode :打开模式
# encoding : 编码格式
# 在 windows 里默认是gbk编码格式打开文件
file = open('xxx.txt', encoding='utf8')
print(file.read())

file.close()
