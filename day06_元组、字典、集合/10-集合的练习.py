#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 18:57
import json

# 1、 去重排序
nums = [1, 3, 5, 2, 4, 2, 6, 6]

x = set(nums)
print(x)
y = list(x)
y.sort(reverse=True)
print(y)

# 2、转换相关的方法
# set(parm)：参数是可迭代对象
m = set(nums)

# python 里有一个比较强大的内置函数，可执行字符串里的代码
# a = 'input("请输入你的姓名：")'
b = '1+1'
# print(eval(a))
print(eval(b))

# json：把列表，元组，字典转换成json字符串 :dumps 方法
person = {'name': 'zhangsan', 'age': 18, 'score': 652.5}
n = json.dumps(person)
print(type(n))
print(n)

s = json.loads(n)
print(type(s))
print(s)
