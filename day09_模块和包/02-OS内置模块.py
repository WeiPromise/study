#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/15 17:53

# os : operationSystem操作系统
# os模块里提供的方法就是用来调用操作系统里的方法的

import os

# 操作系统的名称 windows-> nt 其他-> posix
print(os.name)  # nt
# 路径的分隔符 windows-> \ 其他-> /
print(os.sep)  # \
# 获取文件的绝对路径
print(os.path.abspath('02-OS内置模块.py'))
# 判断是否是文件夹
print(os.path.isdir('02-OS内置模块.py'))
print(os.path.isdir('../day09_模块和包'))

# 判断是否是文件
print(os.path.isfile('02-OS内置模块.py'))
print(os.path.isfile('../day09_模块和包'))

# 判断文件是否存在
print(os.path.exists('02-OS内置模块.py'))
print(os.path.exists('0-常见的内置模块.py'))

file_name = '2020.2.21.demo.py'
# print(file_name.rpartition('.'))
print(os.path.splitext(file_name))

# 获取当前脚本所在文件夹
print(os.getcwd())

# 修改工作目录,没返回值
print(os.chdir('../day08_函数的高阶使用'))
print(os.getcwd())

# 列出摸个文件夹下所有文件名
for file in os.listdir('../day08_函数的高阶使用'):
    print(file)

# 获取环境配置
print(os.environ)

