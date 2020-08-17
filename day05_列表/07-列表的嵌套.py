#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 15:25
import random

nums = [2, 3, 15, [23, 34, 67], 43, 7, 5, 9]

teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'M']

rooms = [[], [], []]

for teacher in teachers:
    room = random.choice(rooms)  # choice 从列表中随机选择一个数据
    room.append(teacher)

print(rooms)
