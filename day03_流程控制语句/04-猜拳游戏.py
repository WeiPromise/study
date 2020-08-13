#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 17:38
import random

player = int(input('请输入 (0)剪刀 (1)石头 (2)布：'))

print('用户:', player)

computer = random.randint(0, 2)

print('电脑:', computer)

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print('牛逼')
elif player == computer:
    print('平局')
else:
    print('垃圾')
