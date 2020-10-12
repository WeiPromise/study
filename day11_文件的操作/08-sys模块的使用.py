#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/7 17:42

# 用来接受用户的输入，和input相关
# sys.stdin
# 标准输出，可以改变默认的输出位置
# sys.stdout
# 可以改变错误输出的默认位置
# sys.stderr

import sys

s_in = sys.stdin

# while True:
#     content = s_in.readline().rstrip('\n')
#     print(content)
#     if content == 'exit':
#         break

sys.stdout = open('stdout.log','w',encoding='utf-8')
print('hello')
print('love')
print('baby')

sys.stderr = open('stderr.log','w',encoding='utf-8')
print(1/0)
print('hahah')
