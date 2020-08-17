#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 16:48

person1 = {'name': 'zhangsan', 'age': 18, 'score': 652.5}
person2 = {'sex': '男'}
person3 = {'name': 'lisi'}

# 添加
person1.update(person2)
# 覆盖
person1.update(person3)

print(person1)
