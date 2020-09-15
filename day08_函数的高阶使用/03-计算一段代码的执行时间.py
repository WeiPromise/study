#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/15 15:49

import time

x = 0

start = time.time()  # 获取当前时间的时间戳
print('start : {}'.format(start))
for i in range(1, 100000000):
    x += i

end = time.time()  # 获取当前时间的时间戳
print('end : {}'.format(end))

cost = end - start
print('cost : {}'.format(cost))
print(x)
