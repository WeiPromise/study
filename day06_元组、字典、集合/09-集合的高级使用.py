#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 18:42

first = {'李白', '杜甫', '白居易', '杜牧', '刘禹锡', '韦应物', '王维'}
second = {'李商隐', '杜牧', '刘长卿', '王维'}
thirt = {'贾岛', '岑参', '孟郊'}

#  - : 差集
print(first - second)

# & ：交集
print(first & second)

# | :并集
print(first | second)

# ^ : 差集的并集（相同的不要）
print(first ^ second)
