#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 16:52

person = {'name': 'zhangsan', 'age': 18, 'score': 652.5}

# 第一种：获取单个key

for key in person:
    print(key, sep='——')

# 第二种：获取所有key

for key in person.keys():
    print(key, sep='——')

for value in person.values():
    print(value, sep='——')

# 第三种：获取所有key-value
for (key, value) in person.items():
    print(key, value, sep='——')

for key, value in person.items():
    print(key, value, sep='——')

