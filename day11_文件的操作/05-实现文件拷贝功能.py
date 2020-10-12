#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/7 14:41

import os

file_name = input('请输入一个文件路径：')

if not os.path.isfile(file_name):
    print('您输入的文件不存在')
    exit(1)

# 打开旧文件
old_file = open(file_name,mode='rb')
# 把旧文件数据取出来写入新文件

names = os.path.splitext(file_name)
new_file_name = '{}.bak{}'.format(names[0],names[1])
new_file = open(new_file_name,'wb')

while True:
    content = old_file.read(1024)
    new_file.write(content)
    if not content:
        break

new_file.close()
old_file.close()