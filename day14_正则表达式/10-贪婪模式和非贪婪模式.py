#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/14 23:28

import re

# 在python的正则表达式里，默认是贪婪模式，尽可能多得匹配

m = re.search(r'm.*a','o3rjmoasdaf')

print(m.group()) # moasda

n = re.search(r'm.*?a','o3rjmoasdaf')

print(n.group()) # moa


m1 = re.match(r'aa(\d+)','aa2343ddd')
print(m1.group(0)) # aa2343
print(m1.group(1)) # 2343
m2 = re.match(r'aa(\d+?)','aa2343ddd')
print(m2.group(0)) # aa2
print(m2.group(1)) # 2
m3 = re.match(r'aa(\d+)ddd','aa2343ddd')
print(m3.group(0)) # aa2343ddd
print(m3.group(1)) # 2343
m4 = re.match(r'aa(\d+?)ddd','aa2343ddd')
print(m4.group(0)) # aa2343ddd
print(m4.group(1)) # 2343

m5 = re.match(r'aa(\d+?).*','aa2343ddd')
print(m5.group(0)) # aa2343ddd
print(m5.group(1)) # 2

m6 = re.match(r'aa(\d??)(.*)','aa2343ddd')
print(m6.group(0)) # aa2343ddd
print(m6.group(1)) # 空
print(m6.group(2)) # 2343ddd

